'''
Classes from the 'SceneKit' framework.
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

    
SCNMTLTessellator = _Class('SCNMTLTessellator')
SCNLevelOfDetail = _Class('SCNLevelOfDetail')
_SCNShadableCompilationIssue = _Class('_SCNShadableCompilationIssue')
SCNShadableHelper = _Class('SCNShadableHelper')
SCNProgram = _Class('SCNProgram')
SCNProgramSemanticInfo = _Class('SCNProgramSemanticInfo')
SCNBufferBinding = _Class('SCNBufferBinding')
SCNIKJoint = _Class('SCNIKJoint')
SCNConstraint = _Class('SCNConstraint')
SCNIKConstraint = _Class('SCNIKConstraint')
SCNTransformConstraint = _Class('SCNTransformConstraint')
SCNConstantScaleConstraint = _Class('SCNConstantScaleConstraint')
SCNBillboardConstraint = _Class('SCNBillboardConstraint')
SCNAvoidOccluderConstraint = _Class('SCNAvoidOccluderConstraint')
SCNSliderConstraint = _Class('SCNSliderConstraint')
SCNAccelerationConstraint = _Class('SCNAccelerationConstraint')
SCNReplicatorConstraint = _Class('SCNReplicatorConstraint')
SCNDistanceConstraint = _Class('SCNDistanceConstraint')
SCNLookAtConstraint = _Class('SCNLookAtConstraint')
SCNJSValueTmpImp = _Class('SCNJSValueTmpImp')
SCNSourceRendererRegistry = _Class('SCNSourceRendererRegistry')
SCNCameraNavigationController = _Class('SCNCameraNavigationController')
SCNEventHandler = _Class('SCNEventHandler')
SCNCameraControlEventHandler = _Class('SCNCameraControlEventHandler')
SCNAuthoringEnvironment = _Class('SCNAuthoringEnvironment')
SCNGeometryElement = _Class('SCNGeometryElement')
SCNGeometrySource = _Class('SCNGeometrySource')
SCNMutableGeometrySource = _Class('SCNMutableGeometrySource')
SCNTransaction = _Class('SCNTransaction')
_SCNUIKitSourceRegistry = _Class('_SCNUIKitSourceRegistry')
SCNBoundingSphere = _Class('SCNBoundingSphere')
SCNBoundingBox = _Class('SCNBoundingBox')
SCNMorpher = _Class('SCNMorpher')
SCNMTLShaderBindingsGenerator = _Class('SCNMTLShaderBindingsGenerator')
SCNMTLArgumentBinder = _Class('SCNMTLArgumentBinder')
_C3DProgressDebugger = _Class('_C3DProgressDebugger')
SCNGeometryTessellator = _Class('SCNGeometryTessellator')
SCNCommonProfileProgramGenerator = _Class('SCNCommonProfileProgramGenerator')
SCNDeferredProgramGeneratorMetal = _Class('SCNDeferredProgramGeneratorMetal')
SCNCommonProfileProgramGeneratorMetal = _Class('SCNCommonProfileProgramGeneratorMetal')
SCNCommonProfileProgramGeneratorGL = _Class('SCNCommonProfileProgramGeneratorGL')
SCNCommonProfileProgramCache = _Class('SCNCommonProfileProgramCache')
USKData_helper = _Class('USKData_helper')
USKObjectPath_helper = _Class('USKObjectPath_helper')
USKToken_helper = _Class('USKToken_helper')
USKHelper = _Class('USKHelper')
C3DEngineNotificationQueueTransientWrapper = _Class('C3DEngineNotificationQueueTransientWrapper')
C3DBinding = _Class('C3DBinding')
SCNPhysicsVehicleWheel = _Class('SCNPhysicsVehicleWheel')
C3DIONSZipFileArchive = _Class('C3DIONSZipFileArchive')
SCNDisplayLink = _Class('SCNDisplayLink')
SCNSkinner = _Class('SCNSkinner')
SCNParticlePropertyController = _Class('SCNParticlePropertyController')
SCNSceneLookUpUnarchiver = _Class('SCNSceneLookUpUnarchiver')
SCNSceneDatabase = _Class('SCNSceneDatabase')
SCNAssetCatalog = _Class('SCNAssetCatalog')
SCNAssetCatalogCacheEntry = _Class('SCNAssetCatalogCacheEntry')
SCNMaterialProperty = _Class('SCNMaterialProperty')
SCNMaterialAttachment = _Class('SCNMaterialAttachment')
SCNCamera = _Class('SCNCamera')
SCNGeometry = _Class('SCNGeometry')
SCNShape = _Class('SCNShape')
SCNText = _Class('SCNText')
SCNTorus = _Class('SCNTorus')
SCNCapsule = _Class('SCNCapsule')
SCNTube = _Class('SCNTube')
SCNCone = _Class('SCNCone')
SCNCylinder = _Class('SCNCylinder')
SCNSphere = _Class('SCNSphere')
SCNPyramid = _Class('SCNPyramid')
SCNBox = _Class('SCNBox')
SCNPlane = _Class('SCNPlane')
SCNMutableGeometry = _Class('SCNMutableGeometry')
SCNFloor = _Class('SCNFloor')
SCNAuthoringEnvironment2 = _Class('SCNAuthoringEnvironment2')
SCNHitTestResult = _Class('SCNHitTestResult')
SCNSceneSource = _Class('SCNSceneSource')
SCNAnimationPlayer = _Class('SCNAnimationPlayer')
SCNAnimation = _Class('SCNAnimation')
SCNTimingFunction = _Class('SCNTimingFunction')
SCNAnimationEvent = _Class('SCNAnimationEvent')
SCNRecursiveLock = _Class('SCNRecursiveLock')
SCNOrderedDictionary = _Class('SCNOrderedDictionary')
SCNRenderer = _Class('SCNRenderer')
SCNOffscreenRenderer = _Class('SCNOffscreenRenderer')
SCNRendererTransitionContext = _Class('SCNRendererTransitionContext')
SCNRendererEvents = _Class('SCNRendererEvents')
SCNRendererViewPoint = _Class('SCNRendererViewPoint')
SCNScene = _Class('SCNScene')
SCNParticleSystem = _Class('SCNParticleSystem')
SCNMaterial = _Class('SCNMaterial')
SCNLight = _Class('SCNLight')
SCNPhysicsWorld = _Class('SCNPhysicsWorld')
SCNMTLLibraryManager = _Class('SCNMTLLibraryManager')
SCNMTLLibrary = _Class('SCNMTLLibrary')
SCNPhysicsBody = _Class('SCNPhysicsBody')
SCNManipulableItem = _Class('SCNManipulableItem')
SCNNodeManipulableItem = _Class('SCNNodeManipulableItem')
SCNMTLMeshElement = _Class('SCNMTLMeshElement')
SCNMTLMesh = _Class('SCNMTLMesh')
SCNMTLComputePipeline = _Class('SCNMTLComputePipeline')
SCNMTLRenderPipeline = _Class('SCNMTLRenderPipeline')
SCNMTLShadable = _Class('SCNMTLShadable')
SCNMTLResourceBinding = _Class('SCNMTLResourceBinding')
SCNMTLPassResourceBinding = _Class('SCNMTLPassResourceBinding')
SCNMTLSemanticResourceBinding = _Class('SCNMTLSemanticResourceBinding')
SCNSpriteKitEventHandler = _Class('SCNSpriteKitEventHandler')
SCNActionTargetState = _Class('SCNActionTargetState')
SCNCameraController = _Class('SCNCameraController')
SCNWeakPointer = _Class('SCNWeakPointer')
SCNStatisticsProvider = _Class('SCNStatisticsProvider')
SCNMTLBufferAllocator = _Class('SCNMTLBufferAllocator')
SCNFixedSizePage = _Class('SCNFixedSizePage')
SCNMTLBuffer = _Class('SCNMTLBuffer')
SCNMTLBufferAllocatorSubBuffer = _Class('SCNMTLBufferAllocatorSubBuffer')
SCNMTLRenderContext = _Class('SCNMTLRenderContext')
SCNNode = _Class('SCNNode')
SCNReferenceNode = _Class('SCNReferenceNode')
SCNNodeReference = _Class('SCNNodeReference')
SCNPhysicsShape = _Class('SCNPhysicsShape')
SCNPass = _Class('SCNPass')
SCNPassContext = _Class('SCNPassContext')
SCNTechnique = _Class('SCNTechnique')
SCNRenderTarget = _Class('SCNRenderTarget')
SCNMTLResourceManager = _Class('SCNMTLResourceManager')
SCNMetalWireframeResource = _Class('SCNMetalWireframeResource')
SCNMTLShadableKey = _Class('SCNMTLShadableKey')
SCNNodeWeakComponent = _Class('SCNNodeWeakComponent')
SCNNodeComponent = _Class('SCNNodeComponent')
C3DAnimationBinding = _Class('C3DAnimationBinding')
SCNPhysicsContact = _Class('SCNPhysicsContact')
SCNManipulator = _Class('SCNManipulator')
SCNPhysicsBehavior = _Class('SCNPhysicsBehavior')
SCNPhysicsVehicle = _Class('SCNPhysicsVehicle')
SCNPhysicsSliderJoint = _Class('SCNPhysicsSliderJoint')
SCNPhysicsConeTwistJoint = _Class('SCNPhysicsConeTwistJoint')
SCNPhysicsBallSocketJoint = _Class('SCNPhysicsBallSocketJoint')
SCNPhysicsCharacter = _Class('SCNPhysicsCharacter')
SCNPhysicsHingeJoint = _Class('SCNPhysicsHingeJoint')
SCNJitterer = _Class('SCNJitterer')
SCNPhysicsField = _Class('SCNPhysicsField')
SCNPhysicsNoiseField = _Class('SCNPhysicsNoiseField')
SCNPhysicsTurbulenceField = _Class('SCNPhysicsTurbulenceField')
SCNPhysicsVortexField = _Class('SCNPhysicsVortexField')
SCNPhysicsCustomField = _Class('SCNPhysicsCustomField')
SCNPhysicsDragField = _Class('SCNPhysicsDragField')
SCNPhysicsElectricField = _Class('SCNPhysicsElectricField')
SCNPhysicsMagneticField = _Class('SCNPhysicsMagneticField')
SCNPhysicsSpringField = _Class('SCNPhysicsSpringField')
SCNPhysicsRadialGravityField = _Class('SCNPhysicsRadialGravityField')
SCNPhysicsLinearGravityField = _Class('SCNPhysicsLinearGravityField')
SCNMTLSkin = _Class('SCNMTLSkin')
SCNMTLMorph = _Class('SCNMTLMorph')
SCNTextureSource = _Class('SCNTextureSource')
SCNCaptureDeviceOutputConsumerSource = _Class('SCNCaptureDeviceOutputConsumerSource')
SCNCaptureDeviceSource = _Class('SCNCaptureDeviceSource')
SCNAVPlayerSource = _Class('SCNAVPlayerSource')
SCNMaterialPropertyTextureProviderSource = _Class('SCNMaterialPropertyTextureProviderSource')
SCNTextureOffscreenRenderingSource = _Class('SCNTextureOffscreenRenderingSource')
SCNTextureDelegateSource = _Class('SCNTextureDelegateSource')
SCNTextureSpriteKitSource = _Class('SCNTextureSpriteKitSource')
SCNTextureCoreAnimationSource = _Class('SCNTextureCoreAnimationSource')
SCNTextureUIKitSource = _Class('SCNTextureUIKitSource')
SCNImageSource = _Class('SCNImageSource')
SCNDelegateSource = _Class('SCNDelegateSource')
SCNUIKitSource = _Class('SCNUIKitSource')
SCNSpriteKitSource = _Class('SCNSpriteKitSource')
SCNCoreAnimationSource = _Class('SCNCoreAnimationSource')
SCNAudioSource = _Class('SCNAudioSource')
SCNAudioPlayer = _Class('SCNAudioPlayer')
SCNAction = _Class('SCNAction')
SCNActionRepeat = _Class('SCNActionRepeat')
SCNActionRemove = _Class('SCNActionRemove')
SCNActionScale = _Class('SCNActionScale')
SCNActionRotate = _Class('SCNActionRotate')
SCNActionMove = _Class('SCNActionMove')
SCNActionSequence = _Class('SCNActionSequence')
SCNActionCustom = _Class('SCNActionCustom')
SCNActionFade = _Class('SCNActionFade')
SCNActionRunAction = _Class('SCNActionRunAction')
SCNActionJavaScript = _Class('SCNActionJavaScript')
SCNActionPerformSelector = _Class('SCNActionPerformSelector')
SCNActionGroup = _Class('SCNActionGroup')
SCNActionReference = _Class('SCNActionReference')
SCNActionWait = _Class('SCNActionWait')
SCNActionPlaySound = _Class('SCNActionPlaySound')
SCNActionRunBlock = _Class('SCNActionRunBlock')
SCNActionHide = _Class('SCNActionHide')
SCNJSImage = _Class('SCNJSImage')
SCNKeyedArchiver = _Class('SCNKeyedArchiver')
SCNKeyedUnarchiver = _Class('SCNKeyedUnarchiver')
SCNAnimationReference = _Class('SCNAnimationReference')
SCN_CAKeyframeAnimation = _Class('SCN_CAKeyframeAnimation')
SCNLowLatencyMetalLayer = _Class('SCNLowLatencyMetalLayer')
SCNMetalLayer = _Class('SCNMetalLayer')
SCNExportOperation = _Class('SCNExportOperation')
_SCNExportOperation = _Class('_SCNExportOperation')
SCNMovieExportOperation = _Class('SCNMovieExportOperation')
SCNView = _Class('SCNView')
_SCNSnapshotWindow = _Class('_SCNSnapshotWindow')
_SCNUIApplicationObserver = _Class('_SCNUIApplicationObserver')
SCNJSValue = _Class('SCNJSValue')
