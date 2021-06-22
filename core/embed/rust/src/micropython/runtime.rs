use core::mem::MaybeUninit;

use cstr_core::CStr;

use super::{ffi, obj::Obj};

pub fn raise_value_error(msg: &'static CStr) -> ! {
    unsafe {
        ffi::mp_raise_ValueError(msg.as_ptr());
    }
    panic!();
}

pub fn call_except<F, T>(mut func: F) -> Result<T, Obj>
where
    F: FnMut() -> T,
{
    unsafe {
        let mut result = MaybeUninit::zeroed();
        let mut wrapper = || {
            result = MaybeUninit::new(func());
        };
        let (callback, argument) = split_func_into_callback_and_argument(&mut wrapper);
        let exception = ffi::trezor_obj_call_protected(Some(callback), argument);
        if exception == Obj::const_none() {
            Ok(result.assume_init())
        } else {
            Err(exception)
        }
    }
}

type ProtectedArgument = *mut cty::c_void;
type ProtectedCallback = unsafe extern "C" fn(ProtectedArgument);

fn split_func_into_callback_and_argument<F>(func: &mut F) -> (ProtectedCallback, ProtectedArgument)
where
    F: FnMut(),
{
    (trampoline::<F>, func as *mut _ as *mut _)
}

unsafe extern "C" fn trampoline<F>(arg: ProtectedArgument)
where
    F: FnMut(),
{
    let func = arg as *mut F;
    unsafe {
        (*func)();
    }
}
