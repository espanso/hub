
# AspNet Boilerplate and Asp Zero Hub

A package to include AspNet Boilerplate and Asp Zero shortcut code generation in espanso.

## Usage

| Keyword             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| :bundle | npm run create-bundles |
| ;;ajax | return abp ajax code  |
| ;;ns | return abp.notify.success |
| ;;ni | return abp.notify.info | 
| ;;nw | return abp.notify.warn | 
| ;;ne | return abp.notify.error | 
| ;;ms | return abp.message.success |
| ;;mi | return abp.message.info | 
| ;;mw | return abp.message.warn | 
| ;;me | return abp.message.error | 
| ;;con | return abp.message.confirm | 
| ;;sbusy | return abp.ui.setBusy | 
| ;;sclear | return abp.ui.clearBusy | 
| ;;sbajax | return abp.ui.setBusy with ajax | 
| ;;bpage | return abp.ui.block | 
| ;;ubpage | return abp.ui.unblock | 
| ;;belm | return abp.ui.block with selector element | 
| ;;ubelm | return abp.ui.unblock with selector element | 
| ;;fstr | return abp.utils.formatString |
| ;;dlog | return abp.log.debug | 
| ;;ilog | return abp.log.info | 
| ;;wlog | return abp.log.warn | 
| ;;elog | return abp.log.error | 
| ;;flog | return abp.log.fatal | 
| ;;getpassive | return disable filter soft delete using block | 
| ;;fkatr | return ForeignKey Attribute | 
| ;;autatr | return AbpAuthorize Attribute | 
| ;;anonatr | return AbpAllowAnonymous or AllowAnonymous Attribute | 
| ;;autatr | return Audited or DisableAuditing Attribute | 
| ;;usecase | return UseCase Attribute | 
| ;;remsatr | return RemoteService (IsEnabled = false) or (IsMetadataEnabled = false) Attribute | 
| ;;vatr | return DisableValidation or EnableValidation Attribute | 
| ;;uow | return UnitOfWork or parameter (IsDisabled = true) or parameter (isTransactional: false) Attribute |
| ;;map | return AutoMapTo Attribute | 
| ;;slattr | return StringLength (MaxLength) or (MaxLength and MinLength) Attribute | 
| ;;grant | return abp.auth.isGranted or razor IsGranted if block | 
| ;;gloc | return app.localize or razor @L("") or L("")  | 
| ;;loc | return xml localization new record  | 
| ;;throw | return throw code UserFriendlyException or Exception | 