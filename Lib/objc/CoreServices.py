'''
Classes from the 'CoreServices' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
_LSCoreTypesRecordProxy = _Class('_LSCoreTypesRecordProxy')
_LSOpenCopierContext = _Class('_LSOpenCopierContext')
_LSBindingForLog = _Class('_LSBindingForLog')
_LSPersonaDatabase = _Class('_LSPersonaDatabase')
_LSOpenConfiguration = _Class('_LSOpenConfiguration')
_LSURLOverride = _Class('_LSURLOverride')
LSApplicationRestrictionsManager = _Class('LSApplicationRestrictionsManager')
_LSCanOpenURLManager = _Class('_LSCanOpenURLManager')
_LSSpringBoardCall = _Class('_LSSpringBoardCall')
_LSOpenResourceOperationDelegateWrapper = _Class('_LSOpenResourceOperationDelegateWrapper')
_LSInstallationService = _Class('_LSInstallationService')
_LSDisplayNameConstructor = _Class('_LSDisplayNameConstructor')
LSAltIconManager = _Class('LSAltIconManager')
_LSAppLinkOpenState = _Class('_LSAppLinkOpenState')
LSDatabaseContext = _Class('LSDatabaseContext')
LSClaimBindingConfiguration = _Class('LSClaimBindingConfiguration')
LSClaimBinding = _Class('LSClaimBinding')
_LSStringLocalizer = _Class('_LSStringLocalizer')
_LSInstallOperationChoke = _Class('_LSInstallOperationChoke')
_LSInstallationOperation = _Class('_LSInstallationOperation')
_LSInstallationManager = _Class('_LSInstallationManager')
_LSDatabase = _Class('_LSDatabase')
_LSChangeObserver = _Class('_LSChangeObserver')
LSApplicationWorkspaceObserver = _Class('LSApplicationWorkspaceObserver')
_LSInstallNotificationJournaller = _Class('_LSInstallNotificationJournaller')
_LSJournalledNotification = _Class('_LSJournalledNotification')
_LSInstallProgressService = _Class('_LSInstallProgressService')
_LSStartupJournalledNotification = _Class('_LSStartupJournalledNotification')
LSInstallProgressObserver = _Class('LSInstallProgressObserver')
LSInstallProgressList = _Class('LSInstallProgressList')
LSProgressNotificationTimer = _Class('LSProgressNotificationTimer')
LSAppLink = _Class('LSAppLink')
_LSSharedWebCredentialsAppLink = _Class('_LSSharedWebCredentialsAppLink')
_LSAppLinkPlugIn = _Class('_LSAppLinkPlugIn')
_LSSharedWebCredentialsAppLinkPlugIn = _Class('_LSSharedWebCredentialsAppLinkPlugIn')
_LSEnumeratedBundleInfo = _Class('_LSEnumeratedBundleInfo')
LSApplicationWorkspaceRemoteObserver = _Class('LSApplicationWorkspaceRemoteObserver')
LSApplicationWorkspace = _Class('LSApplicationWorkspace')
_LSDispatchWithTimeoutResult = _Class('_LSDispatchWithTimeoutResult')
_LSDClient = _Class('_LSDClient')
_LSDModifyClient = _Class('_LSDModifyClient')
_LSDOpenClient = _Class('_LSDOpenClient')
_LSDDeviceIdentifierClient = _Class('_LSDDeviceIdentifierClient')
_LSDReadClient = _Class('_LSDReadClient')
_LSDIconClient = _Class('_LSDIconClient')
LSRegistrationInfo = _Class('LSRegistrationInfo')
_LSDeviceIdentifierCache = _Class('_LSDeviceIdentifierCache')
LSDatabaseBuilder = _Class('LSDatabaseBuilder')
LSRecordBuilder = _Class('LSRecordBuilder')
LSBundleRecordBuilder = _Class('LSBundleRecordBuilder')
LSBundleRecordUpdater = _Class('LSBundleRecordUpdater')
_LSInstallerClient = _Class('_LSInstallerClient')
_LSInstaller = _Class('_LSInstaller')
_LSPlistHint = _Class('_LSPlistHint')
_LSLocalQueryResolver = _Class('_LSLocalQueryResolver')
_LSXPCQueryResolver = _Class('_LSXPCQueryResolver')
_LSQueryContext = _Class('_LSQueryContext')
LSAppClipMetadata = _Class('LSAppClipMetadata')
LSiTunesMetadata = _Class('LSiTunesMetadata')
_LSApplicationState = _Class('_LSApplicationState')
__LSRECORD_NULL_PLACEHOLDER__ = _Class('__LSRECORD_NULL_PLACEHOLDER__')
_LSQuery = _Class('_LSQuery')
_LSDocumentProxyBindingQuery = _Class('_LSDocumentProxyBindingQuery')
_LSBundleQuery = _Class('_LSBundleQuery')
_LSApplicationProxyForIdentifierQuery = _Class('_LSApplicationProxyForIdentifierQuery')
_LSApplicationProxiesWithFlagsQuery = _Class('_LSApplicationProxiesWithFlagsQuery')
_LSApplicationProxiesOfTypeQuery = _Class('_LSApplicationProxiesOfTypeQuery')
_LSBundleProxiesOfTypeQuery = _Class('_LSBundleProxiesOfTypeQuery')
_LSCurrentBundleProxyQuery = _Class('_LSCurrentBundleProxyQuery')
_LSAvailableApplicationsForURLQuery = _Class('_LSAvailableApplicationsForURLQuery')
_LSApplicationIsInstalledQuery = _Class('_LSApplicationIsInstalledQuery')
LSPlugInQuery = _Class('LSPlugInQuery')
LSPlugInQueryWithURL = _Class('LSPlugInQueryWithURL')
LSPlugInQueryWithQueryDictionary = _Class('LSPlugInQueryWithQueryDictionary')
LSPlugInQueryWithIdentifier = _Class('LSPlugInQueryWithIdentifier')
_LSBoundIconInfo = _Class('_LSBoundIconInfo')
_LSDiskUsage = _Class('_LSDiskUsage')
_LSValidationToken = _Class('_LSValidationToken')
_LSBundleIDValidationToken = _Class('_LSBundleIDValidationToken')
FSNode = _Class('FSNode')
LSRecord = _Class('LSRecord')
LSClaimRecord = _Class('LSClaimRecord')
_LSLocalizedStringRecord = _Class('_LSLocalizedStringRecord')
LSBundleRecord = _Class('LSBundleRecord')
LSApplicationExtensionRecord = _Class('LSApplicationExtensionRecord')
LSApplicationRecord = _Class('LSApplicationRecord')
LSExtensionPointRecord = _Class('LSExtensionPointRecord')
_LSSynthesizedExtensionPointRecord = _Class('_LSSynthesizedExtensionPointRecord')
UTTypeRecord = _Class('UTTypeRecord')
_UTDynamicTypeRecord = _Class('_UTDynamicTypeRecord')
_UTDeclaredTypeRecord = _Class('_UTDeclaredTypeRecord')
_LSDService = _Class('_LSDService')
_LSDModifyService = _Class('_LSDModifyService')
_LSDOpenService = _Class('_LSDOpenService')
_LSDDeviceIdentifierService = _Class('_LSDDeviceIdentifierService')
_LSDIconService = _Class('_LSDIconService')
_LSDReadService = _Class('_LSDReadService')
_LSDefaults = _Class('_LSDefaults')
_LSQueryResult = _Class('_LSQueryResult')
_LSQueryResultWithPropertyList = _Class('_LSQueryResultWithPropertyList')
LSExtensionPoint = _Class('LSExtensionPoint')
LSResourceProxy = _Class('LSResourceProxy')
LSDocumentProxy = _Class('LSDocumentProxy')
LSBundleProxy = _Class('LSBundleProxy')
LSVPNPluginProxy = _Class('LSVPNPluginProxy')
LSPlugInKitProxy = _Class('LSPlugInKitProxy')
LSApplicationProxy = _Class('LSApplicationProxy')
LSEnumerator = _Class('LSEnumerator')
_LSDBEnumerator = _Class('_LSDBEnumerator')
_LSTypeEnumerator = _Class('_LSTypeEnumerator')
_LSRecordEnumerator = _Class('_LSRecordEnumerator')
_LSExtensionPointRecordEnumerator = _Class('_LSExtensionPointRecordEnumerator')
_LSExtensionPointEnumerator = _Class('_LSExtensionPointEnumerator')
_LSApplicationExtensionRecordEnumerator = _Class('_LSApplicationExtensionRecordEnumerator')
_LSPlugInProxyEnumerator = _Class('_LSPlugInProxyEnumerator')
_LSApplicationRecordEnumerator = _Class('_LSApplicationRecordEnumerator')
_LSApplicationProxyEnumerator = _Class('_LSApplicationProxyEnumerator')
LSPropertyList = _Class('LSPropertyList')
LSBundleInfoCachedValues = _Class('LSBundleInfoCachedValues')
_LSLazyPropertyList = _Class('_LSLazyPropertyList')
_LSAggregatePropertyList = _Class('_LSAggregatePropertyList')
_LSPlugInPropertyList = _Class('_LSPlugInPropertyList')
_LSEmptyPropertyList = _Class('_LSEmptyPropertyList')
_LSDataBackedPropertyList = _Class('_LSDataBackedPropertyList')
_LSDictionaryBackedPropertyList = _Class('_LSDictionaryBackedPropertyList')
