# generated from networks.py.mako
# do not edit manually!
from typing import Iterator


def by_message_name(message_name: str) -> "MessageInfo" | None:
    for m in _messages_iterator():
        if m.message_name == message_name:
            return m
    return None


def by_type_url(type_url: str) -> "MessageInfo" | None:
    for m in _messages_iterator():
        if m.type_url == type_url:
            return m
    return None


class MessageInfo:
    def __init__(
        self, type_url: str, message_name: str
    ) -> None:
        self.type_url = type_url
        self.message_name = message_name


# fmt: off
def _messages_iterator() -> Iterator[MessageInfo]:
    yield MessageInfo(
        type_url="cosmos.authz.v1beta1.MsgExec",
        message_name="CosmosAuthzV1beta1MsgExec"
    )
    yield MessageInfo(
        type_url="cosmos.authz.v1beta1.MsgGrant",
        message_name="CosmosAuthzV1beta1MsgGrant"
    )
    yield MessageInfo(
        type_url="cosmos.authz.v1beta1.MsgRevoke",
        message_name="CosmosAuthzV1beta1MsgRevoke"
    )
    yield MessageInfo(
        type_url="cosmos.bank.v1beta1.MsgMultiSend",
        message_name="CosmosBankV1beta1MsgMultiSend"
    )
    yield MessageInfo(
        type_url="cosmos.bank.v1beta1.MsgSend",
        message_name="CosmosBankV1beta1MsgSend"
    )
    yield MessageInfo(
        type_url="cosmos.crisis.v1beta1.MsgVerifyInvariant",
        message_name="CosmosCrisisV1beta1MsgVerifyInvariant"
    )
    yield MessageInfo(
        type_url="cosmos.distribution.v1beta1.MsgFundCommunityPool",
        message_name="CosmosDistributionV1beta1MsgFundCommunityPool"
    )
    yield MessageInfo(
        type_url="cosmos.distribution.v1beta1.MsgSetWithdrawAddress",
        message_name="CosmosDistributionV1beta1MsgSetWithdrawAddress"
    )
    yield MessageInfo(
        type_url="cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
        message_name="CosmosDistributionV1beta1MsgWithdrawDelegatorReward"
    )
    yield MessageInfo(
        type_url="cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission",
        message_name="CosmosDistributionV1beta1MsgWithdrawValidatorCommission"
    )
    yield MessageInfo(
        type_url="cosmos.evidence.v1beta1.MsgSubmitEvidence",
        message_name="CosmosEvidenceV1beta1MsgSubmitEvidence"
    )
    yield MessageInfo(
        type_url="cosmos.feegrant.v1beta1.MsgGrantAllowance",
        message_name="CosmosFeegrantV1beta1MsgGrantAllowance"
    )
    yield MessageInfo(
        type_url="cosmos.feegrant.v1beta1.MsgRevokeAllowance",
        message_name="CosmosFeegrantV1beta1MsgRevokeAllowance"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1beta1.MsgDeposit",
        message_name="CosmosGovV1beta1MsgDeposit"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1beta1.MsgSubmitProposal",
        message_name="CosmosGovV1beta1MsgSubmitProposal"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1beta1.MsgVote",
        message_name="CosmosGovV1beta1MsgVote"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1beta1.MsgVoteWeighted",
        message_name="CosmosGovV1beta1MsgVoteWeighted"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1.MsgDeposit",
        message_name="CosmosGovV1MsgDeposit"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1.MsgExecLegacyContent",
        message_name="CosmosGovV1MsgExecLegacyContent"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1.MsgSubmitProposal",
        message_name="CosmosGovV1MsgSubmitProposal"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1.MsgVote",
        message_name="CosmosGovV1MsgVote"
    )
    yield MessageInfo(
        type_url="cosmos.gov.v1.MsgVoteWeighted",
        message_name="CosmosGovV1MsgVoteWeighted"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgCreateGroup",
        message_name="CosmosGroupV1MsgCreateGroup"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgCreateGroupPolicy",
        message_name="CosmosGroupV1MsgCreateGroupPolicy"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgCreateGroupWithPolicy",
        message_name="CosmosGroupV1MsgCreateGroupWithPolicy"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgExec",
        message_name="CosmosGroupV1MsgExec"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgLeaveGroup",
        message_name="CosmosGroupV1MsgLeaveGroup"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgSubmitProposal",
        message_name="CosmosGroupV1MsgSubmitProposal"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupAdmin",
        message_name="CosmosGroupV1MsgUpdateGroupAdmin"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupMembers",
        message_name="CosmosGroupV1MsgUpdateGroupMembers"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupMetadata",
        message_name="CosmosGroupV1MsgUpdateGroupMetadata"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupPolicyAdmin",
        message_name="CosmosGroupV1MsgUpdateGroupPolicyAdmin"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicy",
        message_name="CosmosGroupV1MsgUpdateGroupPolicyDecisionPolicy"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgUpdateGroupPolicyMetadata",
        message_name="CosmosGroupV1MsgUpdateGroupPolicyMetadata"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgVote",
        message_name="CosmosGroupV1MsgVote"
    )
    yield MessageInfo(
        type_url="cosmos.group.v1.MsgWithdrawProposal",
        message_name="CosmosGroupV1MsgWithdrawProposal"
    )
    yield MessageInfo(
        type_url="cosmos.nft.v1beta1.MsgSend",
        message_name="CosmosNftV1beta1MsgSend"
    )
    yield MessageInfo(
        type_url="cosmos.slashing.v1beta1.MsgUnjail",
        message_name="CosmosSlashingV1beta1MsgUnjail"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgBeginRedelegate",
        message_name="CosmosStakingV1beta1MsgBeginRedelegate"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgCancelUnbondingDelegation",
        message_name="CosmosStakingV1beta1MsgCancelUnbondingDelegation"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgCreateValidator",
        message_name="CosmosStakingV1beta1MsgCreateValidator"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgDelegate",
        message_name="CosmosStakingV1beta1MsgDelegate"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgEditValidator",
        message_name="CosmosStakingV1beta1MsgEditValidator"
    )
    yield MessageInfo(
        type_url="cosmos.staking.v1beta1.MsgUndelegate",
        message_name="CosmosStakingV1beta1MsgUndelegate"
    )
    yield MessageInfo(
        type_url="cosmos.upgrade.v1beta1.MsgCancelUpgrade",
        message_name="CosmosUpgradeV1beta1MsgCancelUpgrade"
    )
    yield MessageInfo(
        type_url="cosmos.upgrade.v1beta1.MsgSoftwareUpgrade",
        message_name="CosmosUpgradeV1beta1MsgSoftwareUpgrade"
    )
    yield MessageInfo(
        type_url="cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount",
        message_name="CosmosVestingV1beta1MsgCreatePeriodicVestingAccount"
    )
    yield MessageInfo(
        type_url="cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccount",
        message_name="CosmosVestingV1beta1MsgCreatePermanentLockedAccount"
    )
    yield MessageInfo(
        type_url="cosmos.vesting.v1beta1.MsgCreateVestingAccount",
        message_name="CosmosVestingV1beta1MsgCreateVestingAccount"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgClearAdmin",
        message_name="CosmwasmWasmV1MsgClearAdmin"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgExecuteContract",
        message_name="CosmwasmWasmV1MsgExecuteContract"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgInstantiateContract",
        message_name="CosmwasmWasmV1MsgInstantiateContract"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgMigrateContract",
        message_name="CosmwasmWasmV1MsgMigrateContract"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgStoreCode",
        message_name="CosmwasmWasmV1MsgStoreCode"
    )
    yield MessageInfo(
        type_url="cosmwasm.wasm.v1.MsgUpdateAdmin",
        message_name="CosmwasmWasmV1MsgUpdateAdmin"
    )
    yield MessageInfo(
        type_url="ibc.applications.fee.v1.MsgPayPacketFee",
        message_name="IbcApplicationsFeeV1MsgPayPacketFee"
    )
    yield MessageInfo(
        type_url="ibc.applications.fee.v1.MsgPayPacketFeeAsync",
        message_name="IbcApplicationsFeeV1MsgPayPacketFeeAsync"
    )
    yield MessageInfo(
        type_url="ibc.applications.fee.v1.MsgRegisterCounterpartyAddress",
        message_name="IbcApplicationsFeeV1MsgRegisterCounterpartyAddress"
    )
    yield MessageInfo(
        type_url="ibc.applications.transfer.v1.MsgTransfer",
        message_name="IbcApplicationsTransferV1MsgTransfer"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgAcknowledgement",
        message_name="IbcCoreChannelV1MsgAcknowledgement"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelCloseConfirm",
        message_name="IbcCoreChannelV1MsgChannelCloseConfirm"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelCloseInit",
        message_name="IbcCoreChannelV1MsgChannelCloseInit"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelOpenAck",
        message_name="IbcCoreChannelV1MsgChannelOpenAck"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelOpenConfirm",
        message_name="IbcCoreChannelV1MsgChannelOpenConfirm"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelOpenInit",
        message_name="IbcCoreChannelV1MsgChannelOpenInit"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgChannelOpenTry",
        message_name="IbcCoreChannelV1MsgChannelOpenTry"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgRecvPacket",
        message_name="IbcCoreChannelV1MsgRecvPacket"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgTimeout",
        message_name="IbcCoreChannelV1MsgTimeout"
    )
    yield MessageInfo(
        type_url="ibc.core.channel.v1.MsgTimeoutOnClose",
        message_name="IbcCoreChannelV1MsgTimeoutOnClose"
    )
    yield MessageInfo(
        type_url="ibc.core.client.v1.MsgCreateClient",
        message_name="IbcCoreClientV1MsgCreateClient"
    )
    yield MessageInfo(
        type_url="ibc.core.client.v1.MsgSubmitMisbehaviour",
        message_name="IbcCoreClientV1MsgSubmitMisbehaviour"
    )
    yield MessageInfo(
        type_url="ibc.core.client.v1.MsgUpdateClient",
        message_name="IbcCoreClientV1MsgUpdateClient"
    )
    yield MessageInfo(
        type_url="ibc.core.client.v1.MsgUpgradeClient",
        message_name="IbcCoreClientV1MsgUpgradeClient"
    )
    yield MessageInfo(
        type_url="ibc.core.connection.v1.MsgConnectionOpenAck",
        message_name="IbcCoreConnectionV1MsgConnectionOpenAck"
    )
    yield MessageInfo(
        type_url="ibc.core.connection.v1.MsgConnectionOpenConfirm",
        message_name="IbcCoreConnectionV1MsgConnectionOpenConfirm"
    )
    yield MessageInfo(
        type_url="ibc.core.connection.v1.MsgConnectionOpenInit",
        message_name="IbcCoreConnectionV1MsgConnectionOpenInit"
    )
    yield MessageInfo(
        type_url="ibc.core.connection.v1.MsgConnectionOpenTry",
        message_name="IbcCoreConnectionV1MsgConnectionOpenTry"
    )
    yield MessageInfo(
        type_url="secret.compute.v1beta1.MsgExecuteContract",
        message_name="SecretComputeV1beta1MsgExecuteContract"
    )
    yield MessageInfo(
        type_url="secret.compute.v1beta1.MsgInstantiateContract",
        message_name="SecretComputeV1beta1MsgInstantiateContract"
    )
    yield MessageInfo(
        type_url="secret.compute.v1beta1.MsgStoreCode",
        message_name="SecretComputeV1beta1MsgStoreCode"
    )
    yield MessageInfo(
        type_url="secret.intertx.v1beta1.MsgRegisterAccount",
        message_name="SecretIntertxV1beta1MsgRegisterAccount"
    )
    yield MessageInfo(
        type_url="secret.intertx.v1beta1.MsgSubmitTx",
        message_name="SecretIntertxV1beta1MsgSubmitTx"
    )
    yield MessageInfo(
        type_url="tendermint.liquidity.v1beta1.MsgCreatePool",
        message_name="TendermintLiquidityV1beta1MsgCreatePool"
    )
    yield MessageInfo(
        type_url="tendermint.liquidity.v1beta1.MsgDepositWithinBatch",
        message_name="TendermintLiquidityV1beta1MsgDepositWithinBatch"
    )
    yield MessageInfo(
        type_url="tendermint.liquidity.v1beta1.MsgSwapWithinBatch",
        message_name="TendermintLiquidityV1beta1MsgSwapWithinBatch"
    )
    yield MessageInfo(
        type_url="tendermint.liquidity.v1beta1.MsgWithdrawWithinBatch",
        message_name="TendermintLiquidityV1beta1MsgWithdrawWithinBatch"
    )
    yield MessageInfo(
        type_url="terra.market.v1beta1.MsgSwap",
        message_name="TerraMarketV1beta1MsgSwap"
    )
    yield MessageInfo(
        type_url="terra.market.v1beta1.MsgSwapSend",
        message_name="TerraMarketV1beta1MsgSwapSend"
    )
    yield MessageInfo(
        type_url="terra.oracle.v1beta1.MsgAggregateExchangeRatePrevote",
        message_name="TerraOracleV1beta1MsgAggregateExchangeRatePrevote"
    )
    yield MessageInfo(
        type_url="terra.oracle.v1beta1.MsgAggregateExchangeRateVote",
        message_name="TerraOracleV1beta1MsgAggregateExchangeRateVote"
    )
    yield MessageInfo(
        type_url="terra.oracle.v1beta1.MsgDelegateFeedConsent",
        message_name="TerraOracleV1beta1MsgDelegateFeedConsent"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgClearContractAdmin",
        message_name="TerraWasmV1beta1MsgClearContractAdmin"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgExecuteContract",
        message_name="TerraWasmV1beta1MsgExecuteContract"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgInstantiateContract",
        message_name="TerraWasmV1beta1MsgInstantiateContract"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgMigrateCode",
        message_name="TerraWasmV1beta1MsgMigrateCode"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgMigrateContract",
        message_name="TerraWasmV1beta1MsgMigrateContract"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgStoreCode",
        message_name="TerraWasmV1beta1MsgStoreCode"
    )
    yield MessageInfo(
        type_url="terra.wasm.v1beta1.MsgUpdateContractAdmin",
        message_name="TerraWasmV1beta1MsgUpdateContractAdmin"
    )
