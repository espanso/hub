# AspNet Boilerplate and AspNet Zero Hub

A package to include AspNet Boilerplate and AspNet Zero shortcut code generation in espanso.

**Note** : Sometimes it has been observed that the replace process does not work in Visual Studio. When you run Espanso as an administrator or if you set "backend: Clipboard" in the "default.yml" file located in "espanso\config", the problem is solved.

## Usage

| Keyword      | Description                                                                       |
| ------------ | --------------------------------------------------------------------------------- |
| :bundle      | npm run create-bundles                                                            |
| ::ajax       | return abp ajax code                                                              |
| ::ns         | return abp.notify.success                                                         |
| ::ni         | return abp.notify.info                                                            |
| ::nw         | return abp.notify.warn                                                            |
| ::ne         | return abp.notify.error                                                           |
| ::ms         | return abp.message.success                                                        |
| ::mi         | return abp.message.info                                                           |
| ::mw         | return abp.message.warn                                                           |
| ::me         | return abp.message.error                                                          |
| ::mcon       | return abp.message.confirm                                                        |
| ::sbusy      | return abp.ui.setBusy                                                             |
| ::sclear     | return abp.ui.clearBusy                                                           |
| ::sbajax     | return abp.ui.setBusy with ajax                                                   |
| ::bpage      | return abp.ui.block                                                               |
| ::ubpage     | return abp.ui.unblock                                                             |
| ::belm       | return abp.ui.block with selector element                                         |
| ::ubelm      | return abp.ui.unblock with selector element                                       |
| ::fstr       | return abp.utils.formatString                                                     |
| ::dlog       | return abp.log.debug                                                              |
| ::ilog       | return abp.log.info                                                               |
| ::wlog       | return abp.log.warn                                                               |
| ::elog       | return abp.log.error                                                              |
| ::flog       | return abp.log.fatal                                                              |
| ::getpassive | return disable filter soft delete using block                                     |
| ::fkatr      | return ForeignKey Attribute                                                       |
| ::autatr     | return AbpAuthorize Attribute (3 choices)                                         |
| ::anonatr    | return AbpAllowAnonymous or AllowAnonymous Attribute                              |
| ::audatr     | return Audited or DisableAuditing Attribute                                       |
| ::usecase    | return UseCase Attribute                                                          |
| ::remsatr    | return RemoteService (IsEnabled = false) or (IsMetadataEnabled = false) Attribute |
| ::vatr       | return DisableValidation or EnableValidation Attribute                            |
| ::uow        | return UnitOfWork (5 choices)                                                     |
| ::map        | return AutoMapTo Attribute                                                        |
| ::slattr     | return StringLength (MaxLength) or (MaxLength and MinLength) Attribute            |
| ::grant      | return abp.auth.isGranted or razor IsGranted if block                             |
| ::gloc       | return app.localize or razor @L("") or L("")                                      |
| ::loc        | return xml localization new record                                                |
| ::throw      | return throw code UserFriendlyException or Exception                              |
| ::disdatenor | return DisableDateTimeNormalization Attribute                                     |
| ::abpsession | return AbpSession Property Or Interface Implement                                 |
| ::cache      | return cache Interface Implement                                                  |
| ::dowrap     | return WrapResult Attribute (3 choices)                                           |
| ::dontwrap   | return DontWrapResult Attribute                                                   |
