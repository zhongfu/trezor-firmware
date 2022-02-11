use crate::ui::{
    component::{Component, Event, EventCtx},
    geometry::{Grid, GridCells, Rect},
};

pub struct GridPlaced<T> {
    inner: T,
    grid: Grid,
    cells: GridCells,
}

impl<T> GridPlaced<T> {
    pub fn new(inner: T) -> Self {
        Self {
            inner,
            grid: Grid::new(Rect::zero(), 0, 0),
            cells: GridCells {
                a: (0, 0),
                b: (0, 0),
            },
        }
    }

    pub fn with_grid(mut self, rows: usize, cols: usize) -> Self {
        self.grid.rows = rows;
        self.grid.cols = cols;
        self
    }

    pub fn with_spacing(mut self, spacing: i32) -> Self {
        self.grid.spacing = spacing;
        self
    }

    pub fn with_row_col(mut self, row: usize, col: usize) -> Self {
        self.cells.a = (row, col);
        self.cells.b = (row, col);
        self
    }

    pub fn with_from_to(mut self, a: (usize, usize), b: (usize, usize)) -> Self {
        self.cells.a = a;
        self.cells.b = b;
        self
    }
}

impl<T> Component for GridPlaced<T>
where
    T: Component,
{
    type Msg = T::Msg;

    fn place(&mut self, bounds: Rect) -> Rect {
        self.grid.area = bounds;
        self.inner.place(self.grid.cells(self.cells))
    }

    fn event(&mut self, ctx: &mut EventCtx, event: Event) -> Option<Self::Msg> {
        self.inner.event(ctx, event)
    }

    fn paint(&mut self) {
        self.inner.paint()
    }
}

#[cfg(feature = "ui_debug")]
impl<T> crate::trace::Trace for GridPlaced<T>
where
    T: Component,
    T: crate::trace::Trace,
{
    fn trace(&self, d: &mut dyn crate::trace::Tracer) {
        d.open("GridPlaced");
        d.field("inner", &self.inner);
        d.close();
    }
}
