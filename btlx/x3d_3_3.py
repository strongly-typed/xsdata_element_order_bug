from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.design2machine.com"


class RigidBodyContainerField(Enum):
    BODY1 = "body1"
    BODY2 = "body2"
    BODIES = "bodies"


@dataclass
class SceneGraphStructureStatement:
    pass


@dataclass
class X3DboundedObject:
    class Meta:
        name = "X3DBoundedObject"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )


@dataclass
class X3Dfield:
    class Meta:
        name = "X3DField"


@dataclass
class X3DmetadataObject:
    class Meta:
        name = "X3DMetadataObject"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DnodeMixedContent:
    class Meta:
        name = "X3DNodeMixedContent"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class X3DpickableObject:
    class Meta:
        name = "X3DPickableObject"

    object_type: List[str] = field(
        default_factory=lambda: [
            "\"ALL\"",
        ],
        metadata={
            "name": "objectType",
            "type": "Attribute",
            "tokens": True,
        }
    )
    pickable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DurlObject:
    class Meta:
        name = "X3DUrlObject"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


class AccessTypeChoices(Enum):
    INITIALIZE_ONLY = "initializeOnly"
    INPUT_ONLY = "inputOnly"
    OUTPUT_ONLY = "outputOnly"
    INPUT_OUTPUT = "inputOutput"


class AppliedParametersChoices(Enum):
    BOUNCE = '"BOUNCE"'
    USER_FRICTION = '"USER_FRICTION"'
    FRICTION_COEFFICIENT_2 = '"FRICTION_COEFFICIENT-2"'
    ERROR_REDUCTION = '"ERROR_REDUCTION"'
    CONSTANT_FORCE = '"CONSTANT_FORCE"'
    SPEED_1 = '"SPEED-1"'
    SPEED_2 = '"SPEED-2"'
    SLIP_1 = '"SLIP-1"'
    SLIP_2 = '"SLIP-2"'


class ClosureTypeChoices(Enum):
    PIE = "PIE"
    CHORD = "CHORD"


class ComponentNameChoices(Enum):
    CORE = "Core"
    CADGEOMETRY = "CADGeometry"
    CUBE_MAP_TEXTURING = "CubeMapTexturing"
    DIS = "DIS"
    ENVIRONMENTAL_EFFECTS = "EnvironmentalEffects"
    ENVIRONMENTAL_SENSOR = "EnvironmentalSensor"
    EVENT_UTILITIES = "EventUtilities"
    FOLLOWERS = "Followers"
    GEOMETRY2_D = "Geometry2D"
    GEOMETRY3_D = "Geometry3D"
    GEOSPATIAL = "Geospatial"
    GROUPING = "Grouping"
    HANIM = "HAnim"
    H_ANIM_1 = "H-Anim"
    INTERPOLATION = "Interpolation"
    KEY_DEVICE_SENSOR = "KeyDeviceSensor"
    LAYERING = "Layering"
    LAYOUT = "Layout"
    LIGHTING = "Lighting"
    NAVIGATION = "Navigation"
    NETWORKING = "Networking"
    NURBS = "NURBS"
    PARTICLE_SYSTEMS = "ParticleSystems"
    PICKING = "Picking"
    POINTING_DEVICE_SENSOR = "PointingDeviceSensor"
    RENDERING = "Rendering"
    RIGID_BODY_PHYSICS = "RigidBodyPhysics"
    SCRIPTING = "Scripting"
    SHADERS = "Shaders"
    SHAPE = "Shape"
    SOUND = "Sound"
    TEXT = "Text"
    TEXTURING = "Texturing"
    TEXTURING3_D = "Texturing3D"
    TIME = "Time"
    VOLUME_RENDERING = "VolumeRendering"


class ContainerFieldChoicesAudioClip(Enum):
    SOURCE = "source"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesColor(Enum):
    COLOR = "color"
    COLOR_RAMP = "colorRamp"


class ContainerFieldChoicesDisentityTypeMapping(Enum):
    MAPPING = "mapping"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesGroupLodshapeTransform(Enum):
    CHILDREN = "children"
    PROXY = "proxy"
    ROOT_NODE = "rootNode"
    SHAPE = "shape"
    SKIN = "skin"


class ContainerFieldChoicesHanimJoint(Enum):
    CHILDREN = "children"
    JOINTS = "joints"
    SKELETON = "skeleton"


class ContainerFieldChoicesHanimSegment(Enum):
    CHILDREN = "children"
    SEGMENTS = "segments"


class ContainerFieldChoicesHanimSite(Enum):
    CHILDREN = "children"
    SITES = "sites"
    SKELETON = "skeleton"
    VIEWPOINTS = "viewpoints"


class ContainerFieldChoicesMetadata(Enum):
    METADATA = "metadata"
    VALUE = "value"


class ContainerFieldChoicesPackagedShader(Enum):
    SHADERS = "shaders"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesShaderPart(Enum):
    PARTS = "parts"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesTextureCoordinate(Enum):
    TEX_COORD = "texCoord"
    TEX_COORD_RAMP = "texCoordRamp"


class ContainerFieldChoicesX3DcoordinateNode(Enum):
    COORD = "coord"
    CONTROL_POINT = "controlPoint"
    SKIN_COORD = "skinCoord"


class ContainerFieldChoicesX3DnormalNode(Enum):
    NORMAL = "normal"
    SKIN_NORMAL = "skinNormal"


class ContainerFieldChoicesX3Dtexture2Dnode(Enum):
    TEXTURE = "texture"
    SOURCE = "source"
    BACK = "back"
    BOTTOM = "bottom"
    FRONT = "front"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BACK_TEXTURE = "backTexture"
    BOTTOM_TEXTURE = "bottomTexture"
    FRONT_TEXTURE = "frontTexture"
    LEFT_TEXTURE = "leftTexture"
    RIGHT_TEXTURE = "rightTexture"
    TOP_TEXTURE = "topTexture"


class ContainerFieldChoicesX3Dtexture3Dnode(Enum):
    GRADIENTS = "gradients"
    SEGMENT_IDENTIFIERS = "segmentIdentifiers"
    SURFACE_NORMALS = "surfaceNormals"
    TEXTURE = "texture"
    VOXELS = "voxels"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesX3DurlObject(Enum):
    CHILDREN = "children"
    WATCH_LIST = "watchList"


class ContainerFieldChoicesX3DUrlObjectTexture(Enum):
    TEXTURE = "texture"
    WATCH_LIST = "watchList"
    SOURCE = "source"
    BACK = "back"
    BOTTOM = "bottom"
    FRONT = "front"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BACK_TEXTURE = "backTexture"
    BOTTOM_TEXTURE = "bottomTexture"
    FRONT_TEXTURE = "frontTexture"
    LEFT_TEXTURE = "leftTexture"
    RIGHT_TEXTURE = "rightTexture"
    TOP_TEXTURE = "topTexture"


class FieldTypeChoices(Enum):
    SFBOOL = "SFBool"
    MFBOOL = "MFBool"
    SFCOLOR = "SFColor"
    MFCOLOR = "MFColor"
    SFCOLOR_RGBA = "SFColorRGBA"
    MFCOLOR_RGBA = "MFColorRGBA"
    SFDOUBLE = "SFDouble"
    MFDOUBLE = "MFDouble"
    SFFLOAT = "SFFloat"
    MFFLOAT = "MFFloat"
    SFIMAGE = "SFImage"
    MFIMAGE = "MFImage"
    SFINT32 = "SFInt32"
    MFINT32 = "MFInt32"
    SFNODE = "SFNode"
    MFNODE = "MFNode"
    SFROTATION = "SFRotation"
    MFROTATION = "MFRotation"
    SFSTRING = "SFString"
    MFSTRING = "MFString"
    SFTIME = "SFTime"
    MFTIME = "MFTime"
    SFVEC2D = "SFVec2d"
    MFVEC2D = "MFVec2d"
    SFVEC2F = "SFVec2f"
    MFVEC2F = "MFVec2f"
    SFVEC3D = "SFVec3d"
    MFVEC3D = "MFVec3d"
    SFVEC3F = "SFVec3f"
    MFVEC3F = "MFVec3f"
    SFVEC4D = "SFVec4d"
    MFVEC4D = "MFVec4d"
    SFVEC4F = "SFVec4f"
    MFVEC4F = "MFVec4f"
    SFMATRIX3D = "SFMatrix3d"
    MFMATRIX3D = "MFMatrix3d"
    SFMATRIX3F = "SFMatrix3f"
    MFMATRIX3F = "MFMatrix3f"
    SFMATRIX4D = "SFMatrix4d"
    MFMATRIX4D = "MFMatrix4d"
    SFMATRIX4F = "SFMatrix4f"
    MFMATRIX4F = "MFMatrix4f"


class FogTypeChoices(Enum):
    LINEAR = "LINEAR"
    EXPONENTIAL = "EXPONENTIAL"


class FontFamilyValues(Enum):
    SANS = '"SANS"'
    SERIF = '"SERIF"'
    TYPEWRITER = '"TYPEWRITER"'


class FontStyleChoices(Enum):
    PLAIN = "PLAIN"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    BOLDITALIC = "BOLDITALIC"


class ForceOutputValues(Enum):
    ALL = '"ALL"'
    NONE = '"NONE"'


class GeneratedCubeMapTextureUpdateChoices(Enum):
    NONE = "NONE"
    NEXT_FRAME_ONLY = "NEXT_FRAME_ONLY"
    ALWAYS = "ALWAYS"


class GeoMetadataKeyValues(Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    COORDINATE_SYSTEM = "coordinateSystem"
    HORIZONTAL_DATUM = "horizontalDatum"
    VERTICAL_DATUM = "verticalDatum"
    ELLIPSOID = "ellipsoid"
    EXTENT = "extent"
    RESOLUTION = "resolution"
    ORIGINATOR = "originator"
    COPYRIGHT = "copyright"
    DATE = "date"
    METADATA_FORMAT = "metadataFormat"
    DATA_URL = "dataUrl"
    DATA_FORMAT = "dataFormat"


class GeoSystemEarthEllipsoidValues(Enum):
    AM = "AM"
    AN = "AN"
    BN = "BN"
    BR = "BR"
    CC = "CC"
    CD = "CD"
    EA = "EA"
    EB = "EB"
    EC = "EC"
    ED = "ED"
    EE = "EE"
    EF = "EF"
    FA = "FA"
    HE = "HE"
    HO = "HO"
    ID = "ID"
    IN = "IN"
    KA = "KA"
    RF = "RF"
    SA = "SA"
    WD = "WD"
    WE = "WE"
    WGS84 = "WGS84"
    ZN = "Zn"
    S = "S"


class GeoSystemSpatialReferenceFrameValues(Enum):
    GD = "GD"
    UTM = "UTM"
    GC = "GC"
    GDC = "GDC"
    GCC = "GCC"


class HanimFeaturePointNameValues(Enum):
    SELLION = "sellion"
    R_INFRAORBITALE = "r_infraorbitale"
    L_INFRAORBITALE = "l_infraorbitale"
    SUPRAMENTON = "supramenton"
    R_TRAGION = "r_tragion"
    R_GONION = "r_gonion"
    L_TRAGION = "l_tragion"
    L_GONION = "l_gonion"
    NUCHALE = "nuchale"
    R_CLAVICALE = "r_clavicale"
    SUPRASTERNALE = "suprasternale"
    L_CLAVICALE = "l_clavicale"
    R_THELION = "r_thelion"
    L_THELION = "l_thelion"
    SUBSTERNALE = "substernale"
    R_RIB10 = "r_rib10"
    R_ASIS = "r_asis"
    L_RIB10 = "l_rib10"
    L_ASIS = "l_asis"
    R_ILIOCRISTALE = "r_iliocristale"
    R_TROCHANTERION = "r_trochanterion"
    L_ILIOCRISTALE = "l_iliocristale"
    L_TROCHANTERION = "l_trochanterion"
    CERVICALE = "cervicale"
    RIB10_MIDSPINE = "rib10_midspine"
    R_PSIS = "r_psis"
    L_PSIS = "l_psis"
    WAIST_PREFERRED_POST = "waist_preferred_post"
    R_ACROMION = "r_acromion"
    R_AXILLA_ANT = "r_axilla_ant"
    R_RADIAL_STYLOID = "r_radial_styloid"
    R_AXILLA_POST = "r_axilla_post"
    R_OLECRANON = "r_olecranon"
    R_HUMERAL_LATERAL_EPICN = "r_humeral_lateral_epicn"
    R_HUMERAL_MEDIAL_EPICN = "r_humeral_medial_epicn"
    R_RADIALE = "r_radiale"
    R_METACARPAL_PHA2 = "r_metacarpal_pha2"
    R_DACTYLION = "r_dactylion"
    R_ULNAR_STYLOID = "r_ulnar_styloid"
    R_METACARPAL_PHA5 = "r_metacarpal_pha5"
    L_ACROMION = "l_acromion"
    L_AXILLA_ANT = "l_axilla_ant"
    L_RADIAL_STYLOID = "l_radial_styloid"
    L_AXILLA_POST = "l_axilla_post"
    L_OLECRANON = "l_olecranon"
    L_HUMERAL_LATERAL_EPICN = "l_humeral_lateral_epicn"
    L_HUMERAL_MEDIAL_EPICN = "l_humeral_medial_epicn"
    L_RADIALE = "l_radiale"
    L_METACARPAL_PHA2 = "l_metacarpal_pha2"
    L_DACTYLION = "l_dactylion"
    L_ULNAR_STYLOID = "l_ulnar_styloid"
    L_METACARPAL_PHA5 = "l_metacarpal_pha5"
    R_KNEE_CREASE = "r_knee_crease"
    R_FEMORAL_LATERAL_EPICN = "r_femoral_lateral_epicn"
    R_FEMORAL_MEDIAL_EPICN = "r_femoral_medial_epicn"
    R_METATARSAL_PHA5 = "r_metatarsal_pha5"
    R_LATERAL_MALLEOLUS = "r_lateral_malleolus"
    R_MEDIAL_MALLEOLUS = "r_medial_malleolus"
    R_SPHYRION = "r_sphyrion"
    R_METATARSAL_PHA1 = "r_metatarsal_pha1"
    R_CALCANEOUS_POST = "r_calcaneous_post"
    R_DIGIT2 = "r_digit2"
    L_KNEE_CREASE = "l_knee_crease"
    L_FEMORAL_LATERAL_EPICN = "l_femoral_lateral_epicn"
    L_FEMORAL_MEDIAL_EPICN = "l_femoral_medial_epicn"
    L_METATARSAL_PHA5 = "l_metatarsal_pha5"
    L_LATERAL_MALLEOLUS = "l_lateral_malleolus"
    L_MEDIAL_MALLEOLUS = "l_medial_malleolus"
    L_SPHYRION = "l_sphyrion"
    L_METATARSAL_PHA1 = "l_metatarsal_pha1"
    L_CALCANEOUS_POST = "l_calcaneous_post"
    L_DIGIT2 = "l_digit2"
    CROTCH = "crotch"
    R_NECK_BASE = "r_neck_base"
    L_NECK_BASE = "l_neck_base"
    NAVEL = "navel"


class HanimHumanoidInfoKeyValues(Enum):
    AUTHOR_NAME = "authorName"
    AUTHOR_EMAIL = "authorEmail"
    COPYRIGHT = "copyright"
    CREATION_DATE = "creationDate"
    USAGE_RESTRICTIONS = "usageRestrictions"
    HUMANOID_VERSION = "humanoidVersion"
    AGE = "age"
    GENDER = "gender"
    HEIGHT = "height"
    WEIGHT = "weight"


class HanimJointNameValues(Enum):
    HUMANOID_ROOT = "humanoid_root"
    SACROILIAC = "sacroiliac"
    L_HIP = "l_hip"
    L_KNEE = "l_knee"
    L_ANKLE = "l_ankle"
    L_SUBTALAR = "l_subtalar"
    L_MIDTARSAL = "l_midtarsal"
    L_METATARSAL = "l_metatarsal"
    R_HIP = "r_hip"
    R_KNEE = "r_knee"
    R_ANKLE = "r_ankle"
    R_SUBTALAR = "r_subtalar"
    R_MIDTARSAL = "r_midtarsal"
    R_METATARSAL = "r_metatarsal"
    VL5 = "vl5"
    VL4 = "vl4"
    VL3 = "vl3"
    VL2 = "vl2"
    VL1 = "vl1"
    VT12 = "vt12"
    VT11 = "vt11"
    VT10 = "vt10"
    VT9 = "vt9"
    VT8 = "vt8"
    VT7 = "vt7"
    VT6 = "vt6"
    VT5 = "vt5"
    VT4 = "vt4"
    VT3 = "vt3"
    VT2 = "vt2"
    VT1 = "vt1"
    VC7 = "vc7"
    VC6 = "vc6"
    VC5 = "vc5"
    VC4 = "vc4"
    VC3 = "vc3"
    VC2 = "vc2"
    VC1 = "vc1"
    SKULLBASE = "skullbase"
    L_EYELID_JOINT = "l_eyelid_joint"
    R_EYELID_JOINT = "r_eyelid_joint"
    L_EYEBALL_JOINT = "l_eyeball_joint"
    R_EYEBALL_JOINT = "r_eyeball_joint"
    L_EYEBROW_JOINT = "l_eyebrow_joint"
    R_EYEBROW_JOINT = "r_eyebrow_joint"
    TEMPOROMANDIBULAR = "temporomandibular"
    L_STERNOCLAVICULAR = "l_sternoclavicular"
    L_ACROMIOCLAVICULAR = "l_acromioclavicular"
    L_SHOULDER = "l_shoulder"
    L_ELBOW = "l_elbow"
    L_WRIST = "l_wrist"
    L_THUMB1 = "l_thumb1"
    L_THUMB2 = "l_thumb2"
    L_THUMB3 = "l_thumb3"
    L_INDEX0 = "l_index0"
    L_INDEX1 = "l_index1"
    L_INDEX2 = "l_index2"
    L_INDEX3 = "l_index3"
    L_MIDDLE0 = "l_middle0"
    L_MIDDLE1 = "l_middle1"
    L_MIDDLE2 = "l_middle2"
    L_MIDDLE3 = "l_middle3"
    L_RING0 = "l_ring0"
    L_RING1 = "l_ring1"
    L_RING2 = "l_ring2"
    L_RING3 = "l_ring3"
    L_PINKY0 = "l_pinky0"
    L_PINKY1 = "l_pinky1"
    L_PINKY2 = "l_pinky2"
    L_PINKY3 = "l_pinky3"
    R_STERNOCLAVICULAR = "r_sternoclavicular"
    R_ACROMIOCLAVICULAR = "r_acromioclavicular"
    R_SHOULDER = "r_shoulder"
    R_ELBOW = "r_elbow"
    R_WRIST = "r_wrist"
    R_THUMB1 = "r_thumb1"
    R_THUMB2 = "r_thumb2"
    R_THUMB3 = "r_thumb3"
    R_INDEX0 = "r_index0"
    R_INDEX1 = "r_index1"
    R_INDEX2 = "r_index2"
    R_INDEX3 = "r_index3"
    R_MIDDLE0 = "r_middle0"
    R_MIDDLE1 = "r_middle1"
    R_MIDDLE2 = "r_middle2"
    R_MIDDLE3 = "r_middle3"
    R_RING0 = "r_ring0"
    R_RING1 = "r_ring1"
    R_RING2 = "r_ring2"
    R_RING3 = "r_ring3"
    R_PINKY0 = "r_pinky0"
    R_PINKY1 = "r_pinky1"
    R_PINKY2 = "r_pinky2"
    R_PINKY3 = "r_pinky3"


class HanimSegmentNameValues(Enum):
    SACRUM = "sacrum"
    PELVIS = "pelvis"
    L_THIGH = "l_thigh"
    L_CALF = "l_calf"
    L_HINDFOOT = "l_hindfoot"
    L_MIDPROXIMAL = "l_midproximal"
    L_MIDDISTAL = "l_middistal"
    L_FOREFOOT = "l_forefoot"
    R_THIGH = "r_thigh"
    R_CALF = "r_calf"
    R_HINDFOOT = "r_hindfoot"
    R_MIDPROXIMAL = "r_midproximal"
    R_MIDDISTAL = "r_middistal"
    R_FOREFOOT = "r_forefoot"
    L5 = "l5"
    L4 = "l4"
    L3 = "l3"
    L2 = "l2"
    L1 = "l1"
    T12 = "t12"
    T11 = "t11"
    T10 = "t10"
    T9 = "t9"
    T8 = "t8"
    T7 = "t7"
    T6 = "t6"
    T5 = "t5"
    T4 = "t4"
    T3 = "t3"
    T2 = "t2"
    T1 = "t1"
    C7 = "c7"
    C6 = "c6"
    C5 = "c5"
    C4 = "c4"
    C3 = "c3"
    C2 = "c2"
    C1 = "c1"
    SKULL = "skull"
    L_EYELID = "l_eyelid"
    R_EYELID = "r_eyelid"
    L_EYEBALL = "l_eyeball"
    R_EYEBALL = "r_eyeball"
    L_EYEBROW = "l_eyebrow"
    R_EYEBROW = "r_eyebrow"
    JAW = "jaw"
    L_CLAVICLE = "l_clavicle"
    L_SCAPULA = "l_scapula"
    L_UPPERARM = "l_upperarm"
    L_FOREARM = "l_forearm"
    L_HAND = "l_hand"
    L_THUMB_METACARPAL = "l_thumb_metacarpal"
    L_THUMB_PROXIMAL = "l_thumb_proximal"
    L_THUMB_DISTAL = "l_thumb_distal"
    L_INDEX_METACARPAL = "l_index_metacarpal"
    L_INDEX_PROXIMAL = "l_index_proximal"
    L_INDEX_MIDDLE = "l_index_middle"
    L_INDEX_DISTAL = "l_index_distal"
    L_MIDDLE_METACARPAL = "l_middle_metacarpal"
    L_MIDDLE_PROXIMAL = "l_middle_proximal"
    L_MIDDLE_MIDDLE = "l_middle_middle"
    L_MIDDLE_DISTAL = "l_middle_distal"
    L_RING_METACARPAL = "l_ring_metacarpal"
    L_RING_PROXIMAL = "l_ring_proximal"
    L_RING_MIDDLE = "l_ring_middle"
    L_RING_DISTAL = "l_ring_distal"
    L_PINKY_METACARPAL = "l_pinky_metacarpal"
    L_PINKY_PROXIMAL = "l_pinky_proximal"
    L_PINKY_MIDDLE = "l_pinky_middle"
    L_PINKY_DISTAL = "l_pinky_distal"
    R_CLAVICLE = "r_clavicle"
    R_SCAPULA = "r_scapula"
    R_UPPERARM = "r_upperarm"
    R_FOREARM = "r_forearm"
    R_HAND = "r_hand"
    R_THUMB_METACARPAL = "r_thumb_metacarpal"
    R_THUMB_PROXIMAL = "r_thumb_proximal"
    R_THUMB_DISTAL = "r_thumb_distal"
    R_INDEX_METACARPAL = "r_index_metacarpal"
    R_INDEX_PROXIMAL = "r_index_proximal"
    R_INDEX_MIDDLE = "r_index_middle"
    R_INDEX_DISTAL = "r_index_distal"
    R_MIDDLE_METACARPAL = "r_middle_metacarpal"
    R_MIDDLE_PROXIMAL = "r_middle_proximal"
    R_MIDDLE_MIDDLE = "r_middle_middle"
    R_MIDDLE_DISTAL = "r_middle_distal"
    R_RING_METACARPAL = "r_ring_metacarpal"
    R_RING_PROXIMAL = "r_ring_proximal"
    R_RING_MIDDLE = "r_ring_middle"
    R_RING_DISTAL = "r_ring_distal"
    R_PINKY_METACARPAL = "r_pinky_metacarpal"
    R_PINKY_PROXIMAL = "r_pinky_proximal"
    R_PINKY_MIDDLE = "r_pinky_middle"
    R_PINKY_DISTAL = "r_pinky_distal"


class HanimVersionChoices(Enum):
    VALUE_1_0 = "1.0"
    VALUE_2_0 = "2.0"


class InitializeOnlyAccessTypes(Enum):
    AUTO_CALC = "autoCalc"
    BBOX_CENTER = "bboxCenter"
    BBOX_SIZE = "bboxSize"
    BEGIN_CAP = "beginCap"
    BOTTOM_RADIUS = "bottomRadius"
    CATEGORY = "category"
    CCW = "ccw"
    CHILD1_URL = "child1Url"
    CHILD2_URL = "child2Url"
    CHILD3_URL = "child3Url"
    CHILD4_URL = "child4Url"
    CLOSED = "closed"
    CLOSURE_TYPE = "closureType"
    COLOR_KEY = "colorKey"
    COLOR_INDEX = "colorIndex"
    COLOR_PER_VERTEX = "colorPerVertex"
    CONVEX = "convex"
    COORD_INDEX = "coordIndex"
    COUNTRY = "country"
    CREASE_ANGLE = "creaseAngle"
    CROSS_SECTION = "crossSection"
    DIRECT_OUTPUT = "directOutput"
    DOMAIN = "domain"
    DURATION = "duration"
    END_CAP = "endCap"
    END_ANGLE = "endAngle"
    EXTRA = "extra"
    FAMILY = "family"
    FORCE_TRANSITIONS = "forceTransitions"
    GENERATE_MIP_MAPS = "generateMipMaps"
    GEO_GRID_ORIGIN = "geoGridOrigin"
    GEOMETRY_TYPE = "geometryType"
    GEO_SYSTEM = "geoSystem"
    HEIGHT = "height"
    HORIZONTAL = "horizontal"
    INDEX = "index"
    INITIAL_DESTINATION = "initialDestination"
    INITIAL_VALUE = "initialValue"
    INNER_RADIUS = "innerRadius"
    INTERNAL = "internal"
    INTERSECTION_TYPE = "intersectionType"
    JUSTIFY = "justify"
    KIND = "kind"
    KNOT = "knot"
    LANGUAGE = "language"
    LEFT_TO_RIGHT = "leftToRight"
    LINE_SEGMENTS = "lineSegments"
    MUST_EVALUATE = "mustEvaluate"
    NORMAL_INDEX = "normalIndex"
    NORMAL_PER_VERTEX = "normalPerVertex"
    NUM_COMPONENTS = "numComponents"
    ORDER = "order"
    OUTER_RADIUS = "outerRadius"
    PHASE_FUNCTION = "phaseFunction"
    POINT_SIZE = "pointSize"
    RADIUS = "radius"
    RANGE = "range"
    REPEAT_R = "repeatR"
    REPEAT_S = "repeatS"
    REPEAT_T = "repeatT"
    ROOT_URL = "rootUrl"
    ROTATE_YUP = "rotateYUp"
    RTP_HEADER_EXPECTED = "rtpHeaderExpected"
    SIDE = "side"
    SIZE = "size"
    SOLID = "solid"
    SORT_ORDER = "sortOrder"
    SPACING = "spacing"
    SPATIALIZE = "spatialize"
    SPECIFIC = "specific"
    SPEED_FACTOR = "speedFactor"
    SPINE = "spine"
    START_ANGLE = "startAngle"
    STYLE = "style"
    SUBCATEGORY = "subcategory"
    SURFACE_AREA = "surfaceArea"
    TEX_COORD_INDEX = "texCoordIndex"
    TEX_COORD_KEY = "texCoordKey"
    TOP_TO_BOTTOM = "topToBottom"
    U_CLOSED = "uClosed"
    U_DIMENSION = "uDimension"
    U_KNOT = "uKnot"
    U_ORDER = "uOrder"
    V_CLOSED = "vClosed"
    V_DIMENSION = "vDimension"
    V_KNOT = "vKnot"
    V_ORDER = "vOrder"
    X_DIMENSION = "xDimension"
    X_SPACING = "xSpacing"
    Z_DIMENSION = "zDimension"
    Z_SPACING = "zSpacing"


class InputOnlyAccessTypes(Enum):
    ACTIVATE = "activate"
    SET_ARTICULATION_PARAMETER_VALUE0 = "set_articulationParameterValue0"
    SET_ARTICULATION_PARAMETER_VALUE1 = "set_articulationParameterValue1"
    SET_ARTICULATION_PARAMETER_VALUE2 = "set_articulationParameterValue2"
    SET_ARTICULATION_PARAMETER_VALUE3 = "set_articulationParameterValue3"
    SET_ARTICULATION_PARAMETER_VALUE4 = "set_articulationParameterValue4"
    SET_ARTICULATION_PARAMETER_VALUE5 = "set_articulationParameterValue5"
    SET_ARTICULATION_PARAMETER_VALUE6 = "set_articulationParameterValue6"
    SET_ARTICULATION_PARAMETER_VALUE7 = "set_articulationParameterValue7"
    SET_BOOLEAN = "set_boolean"
    SET_BIND = "set_bind"
    SET_COLOR_INDEX = "set_colorIndex"
    SET_CONTACTS = "set_contacts"
    SET_COORD_INDEX = "set_coordIndex"
    SET_CROSS_SECTION = "set_crossSection"
    SET_DESTINATION = "set_destination"
    SET_FRACTION = "set_fraction"
    SET_HEIGHT = "set_height"
    SET_INDEX = "set_index"
    SET_NORMAL_INDEX = "set_normalIndex"
    SET_ORIENTATION = "set_orientation"
    SET_SCALE = "set_scale"
    SET_SPINE = "set_spine"
    SET_TEX_COORD_INDEX = "set_texCoordIndex"
    SET_TRIGGER_TIME = "set_triggerTime"


class InputOutputAccessTypes(Enum):
    ACTIVE_LAYER = "activeLayer"
    ADDRESS = "address"
    ALIGN = "align"
    ALPHA = "alpha"
    AMBIENT_INTENSITY = "ambientIntensity"
    ANCHOR_POINT = "anchorPoint"
    ANGLE = "angle"
    ANGULAR_DAMPING_FACTOR = "angularDampingFactor"
    ANGULAR_VELOCITY = "angularVelocity"
    ANISOTROPIC_DEGREE = "anisotropicDegree"
    ANTENNA_LOCATION = "antennaLocation"
    APPLICATION_ID = "applicationID"
    APPLIED = "applied"
    APPLIED_PARAMETERS = "appliedParameters"
    ANTENNA_PATTERN_TYPE = "antennaPatternType"
    ANTENNA_PATTERN_LENGTH = "antennaPatternLength"
    ARTICULATION_PARAMETER_ARRAY = "articulationParameterArray"
    ARTICULATION_PARAMETER_CHANGE_INDICATOR_ARRAY = "articulationParameterChangeIndicatorArray"
    ARTICULATION_PARAMETER_COUNT = "articulationParameterCount"
    ARTICULATION_PARAMETER_DESIGNATOR_ARRAY = "articulationParameterDesignatorArray"
    ARTICULATION_PARAMETER_ID_PART_ATTACHED_TO_ARRAY = "articulationParameterIdPartAttachedToArray"
    ARTICULATION_PARAMETER_TYPE_ARRAY = "articulationParameterTypeArray"
    ATTENUATION = "attenuation"
    AUTO_DAMP = "autoDamp"
    AUTO_DISABLE = "autoDisable"
    AUTO_OFFSET = "autoOffset"
    AVATAR_SIZE = "avatarSize"
    AXIS = "axis"
    AXIS1 = "axis1"
    AXIS1_ANGLE = "axis1Angle"
    AXIS1_TORQUE = "axis1Torque"
    AXIS2 = "axis2"
    AXIS2_ANGLE = "axis2Angle"
    AXIS2_TORQUE = "axis2Torque"
    AXIS3_ANGLE = "axis3Angle"
    AXIS3_TORQUE = "axis3Torque"
    AXIS_OF_ROTATION = "axisOfRotation"
    AXIS_ROTATION = "axisRotation"
    BACK = "back"
    BACK_AMBIENT_INTENSITY = "backAmbientIntensity"
    BACK_DIFFUSE_COLOR = "backDiffuseColor"
    BACK_EMISSIVE_COLOR = "backEmissiveColor"
    BACK_SHININESS = "backShininess"
    BACK_SPECULAR_COLOR = "backSpecularColor"
    BACK_TRANSPARENCY = "backTransparency"
    BACK_URL = "backUrl"
    BEAM_WIDTH = "beamWidth"
    BOTTOM = "bottom"
    BOTTOM_URL = "bottomUrl"
    BOUNCE = "bounce"
    BOUNDARY_OPACITY = "boundaryOpacity"
    BORDER_COLOR = "borderColor"
    BORDER_WIDTH = "borderWidth"
    BOUNDARY_MODE_S = "boundaryModeS"
    BOUNDARY_MODE_T = "boundaryModeT"
    BOUNDARY_MODE_R = "boundaryModeR"
    CENTER = "center"
    CENTER_OF_MASS = "centerOfMass"
    CENTER_OF_ROTATION = "centerOfRotation"
    CLIP_BOUNDARY = "clipBoundary"
    COLLISION_TYPE = "collisionType"
    COLOR = "color"
    COLOR_STEPS = "colorSteps"
    CONTACT_NORMAL = "contactNormal"
    CONTOUR_STEP_SIZE = "contourStepSize"
    CONTROL_POINT = "controlPoint"
    CONSTANT_FORCE_MIX = "constantForceMix"
    CONTACT_SURFACE_THICKNESS = "contactSurfaceThickness"
    COOL_COLOR = "coolColor"
    CREATE_PARTICLES = "createParticles"
    CRYPTO_SYSTEM = "cryptoSystem"
    CRYPTO_KEY_ID = "cryptoKeyID"
    CUT_OFF_ANGLE = "cutOffAngle"
    CYCLE_INTERVAL = "cycleInterval"
    DATA = "data"
    DATA_LENGTH = "dataLength"
    DEAD_RECKONING = "deadReckoning"
    DELETION_ALLOWED = "deletionAllowed"
    DEPTH = "depth"
    DESCRIPTION = "description"
    DESIRED_ANGULAR_VELOCITY1 = "desiredAngularVelocity1"
    DESIRED_ANGULAR_VELOCITY2 = "desiredAngularVelocity2"
    DETONATION_LOCATION = "detonationLocation"
    DETONATION_RELATIVE_LOCATION = "detonationRelativeLocation"
    DETONATION_RESULT = "detonationResult"
    DIFFUSE_COLOR = "diffuseColor"
    DIMENSIONS = "dimensions"
    DIRECTION = "direction"
    DISABLE_ANGULAR_SPEED = "disableAngularSpeed"
    DISABLE_LINEAR_SPEED = "disableLinearSpeed"
    DISABLE_TIME = "disableTime"
    DISK_ANGLE = "diskAngle"
    DISPLACEMENTS = "displacements"
    DISPLAYED = "displayed"
    EASE_IN_EASE_OUT = "easeInEaseOut"
    EDGE_COLOR = "edgeColor"
    EMISSIVE_COLOR = "emissiveColor"
    ENABLED = "enabled"
    ENABLED_AXES = "enabledAxes"
    ENCODING_SCHEME = "encodingScheme"
    ENTITY_ID = "entityID"
    ENTITY_KIND = "entityKind"
    ENTITY_DOMAIN = "entityDomain"
    ENTITY_COUNTRY = "entityCountry"
    ENTITY_CATEGORY = "entityCategory"
    ENTITY_SUBCATEGORY = "entitySubcategory"
    ENTITY_SPECIFIC = "entitySpecific"
    ENTITY_EXTRA = "entityExtra"
    ERROR_CORRECTION = "errorCorrection"
    EVENT_APPLICATION_ID = "eventApplicationID"
    EVENT_ENTITY_ID = "eventEntityID"
    EVENT_NUMBER = "eventNumber"
    EVENT_SITE_ID = "eventSiteID"
    FAN_COUNT = "fanCount"
    FIELD_OF_VIEW = "fieldOfView"
    FILLED = "filled"
    FINITE_ROTATION_AXIS = "finiteRotationAxis"
    FIRED1 = "fired1"
    FIRED2 = "fired2"
    FIRE_MISSION_INDEX = "fireMissionIndex"
    FIRING_RANGE = "firingRange"
    FIRING_RATE = "firingRate"
    FIXED = "fixed"
    FOG_TYPE = "fogType"
    FORCE = "force"
    FORCE_ID = "forceID"
    FORCE_OUTPUT = "forceOutput"
    FORCES = "forces"
    FREQUENCY = "frequency"
    FRICTION_COEFFICIENTS = "frictionCoefficients"
    FRICTION_DIRECTION = "frictionDirection"
    FRONT = "front"
    FRONT_URL = "frontUrl"
    FUNCTION = "function"
    FUSE = "fuse"
    GEO_CENTER = "geoCenter"
    GEO_COORDS = "geoCoords"
    GLOBAL = "global"
    GRADIENT_THRESHOLD = "gradientThreshold"
    GRAVITY = "gravity"
    GROUND_ANGLE = "groundAngle"
    GROUND_COLOR = "groundColor"
    GUSTINESS = "gustiness"
    HATCH_COLOR = "hatchColor"
    HATCHED = "hatched"
    HATCH_STYLE = "hatchStyle"
    HEADLIGHT = "headlight"
    IMAGE = "image"
    INERTIA = "inertia"
    INFO = "info"
    INPUT_SOURCE = "inputSource"
    INTEGER_KEY = "integerKey"
    INTENSITY = "intensity"
    INTENSITY_THRESHOLD = "intensityThreshold"
    ITERATIONS = "iterations"
    IS_PICKABLE = "isPickable"
    KEY = "key"
    KEY_VELOCITY = "keyVelocity"
    JUMP = "jump"
    KEY_VALUE = "keyValue"
    LEFT = "left"
    LEFT_URL = "leftUrl"
    LENGTH = "length"
    LENGTH_OF_MODULATION_PARAMETERS = "lengthOfModulationParameters"
    LIFETIME_VARIATION = "lifetimeVariation"
    LIGHTING = "lighting"
    LIMIT_ORIENTATION = "limitOrientation"
    LINEAR_ACCELERATION = "linearAcceleration"
    LINEAR_DAMPING_FACTOR = "linearDampingFactor"
    LINEAR_VELOCITY = "linearVelocity"
    LINETYPE = "linetype"
    LINEWIDTH_SCALE_FACTOR = "linewidthScaleFactor"
    LLIMIT = "llimit"
    LOAD = "load"
    LOCATION = "location"
    LOOP = "loop"
    MARKING = "marking"
    MASS = "mass"
    MAGNIFICATION_FILTER = "magnificationFilter"
    MATCH_CRITERION = "matchCriterion"
    MATRIX = "matrix"
    MAX_ANGLE = "maxAngle"
    MAX_ANGLE1 = "maxAngle1"
    MAX_BACK = "maxBack"
    MAX_CORRECTION_SPEED = "maxCorrectionSpeed"
    MAX_EXTENT = "maxExtent"
    MAX_FRONT = "maxFront"
    MAX_PARTICLES = "maxParticles"
    MAX_POSITION = "maxPosition"
    MAX_SEPARATION = "maxSeparation"
    MAX_TORQUE1 = "maxTorque1"
    MAX_TORQUE2 = "maxTorque2"
    MIN_ANGLE = "minAngle"
    MIN_ANGLE1 = "minAngle1"
    MIN_BACK = "minBack"
    MIN_BOUNCE_SPEED = "minBounceSpeed"
    MIN_FRONT = "minFront"
    MINIFICATION_FILTER = "minificationFilter"
    MIN_POSITION = "minPosition"
    MIN_SEPARATION = "minSeparation"
    MODE = "mode"
    MODULATION_TYPE_SPREAD_SPECTRUM = "modulationTypeSpreadSpectrum"
    MODULATION_TYPE_MAJOR = "modulationTypeMajor"
    MODULATION_TYPE_DETAIL = "modulationTypeDetail"
    MODULATION_TYPE_SYSTEM = "modulationTypeSystem"
    MOMENTS_OF_INERTIA = "momentsOfInertia"
    MOTOR1_AXIS = "motor1Axis"
    MOTOR2_AXIS = "motor2Axis"
    MOTOR3_AXIS = "motor3Axis"
    MULTICAST_RELAY_HOST = "multicastRelayHost"
    MULTICAST_RELAY_PORT = "multicastRelayPort"
    MUNITION_END_POINT = "munitionEndPoint"
    MUNITION_START_POINT = "munitionStartPoint"
    MUNITION_APPLICATION_ID = "munitionApplicationID"
    MUNITION_ENTITY_ID = "munitionEntityID"
    MUNITION_SITE_ID = "munitionSiteID"
    MUNITION_QUANTITY = "munitionQuantity"
    NAME = "name"
    NETWORK_MODE = "networkMode"
    NORMALIZE_VELOCITY = "normalizeVelocity"
    OBJECT_TYPE = "objectType"
    OFFSET = "offset"
    OFFSET_UNITS = "offsetUnits"
    ON = "on"
    OPACITY_FACTOR = "opacityFactor"
    ORIENTATION = "orientation"
    ORTHOGONAL_COLOR = "orthogonalColor"
    PARALLEL_COLOR = "parallelColor"
    PARAMETER = "parameter"
    PARTICLE_LIFETIME = "particleLifetime"
    PARTICLE_SIZE = "particleSize"
    PAUSE_TIME = "pauseTime"
    PICKABLE = "pickable"
    PITCH = "pitch"
    PLANE = "plane"
    POINT = "point"
    PORT = "port"
    POSITION = "position"
    POWER = "power"
    PREFER_ACCURACY = "preferAccuracy"
    PRIORITY = "priority"
    RADIO_ID = "radioID"
    RADIO_ENTITY_TYPE_KIND = "radioEntityTypeKind"
    RADIO_ENTITY_TYPE_DOMAIN = "radioEntityTypeDomain"
    RADIO_ENTITY_TYPE_COUNTRY = "radioEntityTypeCountry"
    RADIO_ENTITY_TYPE_CATEGORY = "radioEntityTypeCategory"
    RADIO_ENTITY_TYPE_NOMENCLATURE = "radioEntityTypeNomenclature"
    RADIO_ENTITY_TYPE_NOMENCLATURE_VERSION = "radioEntityTypeNomenclatureVersion"
    READ_INTERVAL = "readInterval"
    RECEIVED_POWER = "receivedPower"
    RECEIVER_STATE = "receiverState"
    REFERENCE = "reference"
    RELATIVE_ANTENNA_LOCATION = "relativeAntennaLocation"
    RETAINED_OPACITY = "retainedOpacity"
    RETAIN_USER_OFFSETS = "retainUserOffsets"
    RESUME_TIME = "resumeTime"
    RIGHT = "right"
    RIGHT_URL = "rightUrl"
    ROTATION = "rotation"
    SAMPLE_RATE = "sampleRate"
    SAMPLES = "samples"
    SCALE = "scale"
    SCALE_MODE = "scaleMode"
    SCALE_ORIENTATION = "scaleOrientation"
    SEGMENT_ENABLED = "segmentEnabled"
    SEPARATE_BACK_COLOR = "separateBackColor"
    SHININESS = "shininess"
    SHADOWS = "shadows"
    SILHOUETTE_BOUNDARY_OPACITY = "silhouetteBoundaryOpacity"
    SILHOUETTE_RETAINED_OPACITY = "silhouetteRetainedOpacity"
    SILHOUETTE_SHARPNESS = "silhouetteSharpness"
    SITE_ID = "siteID"
    SIZE_UNITS = "sizeUnits"
    SKIN_COORD_INDEX = "skinCoordIndex"
    SKIN_COORD_WEIGHT = "skinCoordWeight"
    SKY_COLOR = "skyColor"
    SKY_ANGLE = "skyAngle"
    SLIDER_FORCE = "sliderForce"
    SLIP_COEFFICIENTS = "slipCoefficients"
    SLIP_FACTORS = "slipFactors"
    SOFTNESS_CONSTANT_FORCE_MIX = "softnessConstantForceMix"
    SOFTNESS_ERROR_CORRECTION = "softnessErrorCorrection"
    SOURCE = "source"
    SPECULAR_COLOR = "specularColor"
    SPEED = "speed"
    START_TIME = "startTime"
    STIFFNESS = "stiffness"
    STOP_BOUNCE = "stopBounce"
    STOP_ERROR_CORRECTION = "stopErrorCorrection"
    STOP1_CONSTANT_FORCE_MIX = "stop1ConstantForceMix"
    STOP1_BOUNCE = "stop1Bounce"
    STOP2_BOUNCE = "stop2Bounce"
    STOP3_BOUNCE = "stop3Bounce"
    STOP1_ERROR_CORRECTION = "stop1ErrorCorrection"
    STOP2_ERROR_CORRECTION = "stop2ErrorCorrection"
    STOP3_ERROR_CORRECTION = "stop3ErrorCorrection"
    STOP_TIME = "stopTime"
    STRING = "string"
    STRIP_COUNT = "stripCount"
    SUMMARY = "summary"
    SURFACE_SPEED = "surfaceSpeed"
    SURFACE_TOLERANCE = "surfaceTolerance"
    SURFACE_VALUES = "surfaceValues"
    SUSPENSION_ERROR_CORRECTION = "suspensionErrorCorrection"
    SUSPENSION_FORCE = "suspensionForce"
    TAU = "tau"
    TDL_TYPE = "tdlType"
    TESSELLATION = "tessellation"
    TESSELLATION_SCALE = "tessellationScale"
    TEXTURE_COMPRESSION = "textureCompression"
    TEXTURE_PRIORITY = "texturePriority"
    TIME_OUT = "timeOut"
    TITLE = "title"
    TOGGLE = "toggle"
    TOLERANCE = "tolerance"
    TOP = "top"
    TOP_URL = "topUrl"
    TORQUES = "torques"
    TRANSITION_TIME = "transitionTime"
    TRANSITION_TYPE = "transitionType"
    TRANSLATION = "translation"
    TRANSMIT_FREQUENCY_BANDWIDTH = "transmitFrequencyBandwidth"
    TRANSMIT_STATE = "transmitState"
    TRANSMITTER_APPLICATION_ID = "transmitterApplicationID"
    TRANSMITTER_ENTITY_ID = "transmitterEntityID"
    TRANSMITTER_RADIO_ID = "transmitterRadioID"
    TRANSMITTER_SITE_ID = "transmitterSiteID"
    TRANSPARENCY = "transparency"
    TURBULENCE = "turbulence"
    TYPE = "type"
    ULIMIT = "ulimit"
    UPDATE = "update"
    URL = "url"
    USE_FINITE_ROTATION = "useFiniteRotation"
    USE_GEOMETRY = "useGeometry"
    USE_GLOBAL_GRAVITY = "useGlobalGravity"
    U_TESSELLATION = "uTessellation"
    VARIATION = "variation"
    VALUE = "value"
    VERSION = "version"
    VECTOR = "vector"
    VERTEX_COUNT = "vertexCount"
    VERTICES = "vertices"
    VISIBILITY_LIMIT = "visibilityLimit"
    VISIBILITY_RANGE = "visibilityRange"
    VISIBLE = "visible"
    V_TESSELLATION = "vTessellation"
    WARHEAD = "warhead"
    WARM_COLOR = "warmColor"
    WEIGHT = "weight"
    WEIGHT_CONSTANT1 = "weightConstant1"
    WEIGHT_CONSTANT2 = "weightConstant2"
    WEIGHT_FUNCTION1 = "weightFunction1"
    WEIGHT_FUNCTION2 = "weightFunction2"
    WHICH_CHOICE = "whichChoice"
    WHICH_GEOMETRY = "whichGeometry"
    WRITE_INTERVAL = "writeInterval"
    Y_SCALE = "yScale"


class IntersectionTypeValues(Enum):
    BOUNDS = "BOUNDS"
    GEOMETRY = "GEOMETRY"


class JustifyChoices(Enum):
    MIDDLE = '"MIDDLE"'
    MIDDLE_BEGIN = (
            "\"MIDDLE\"",
            "\"BEGIN\"",
        )
    MIDDLE_END = (
            "\"MIDDLE\"",
            "\"END\"",
        )
    MIDDLE_FIRST = (
            "\"MIDDLE\"",
            "\"FIRST\"",
        )
    MIDDLE_MIDDLE = (
            "\"MIDDLE\"",
            "\"MIDDLE\"",
        )
    BEGIN = '"BEGIN"'
    BEGIN_BEGIN = (
            "\"BEGIN\"",
            "\"BEGIN\"",
        )
    BEGIN_END = (
            "\"BEGIN\"",
            "\"END\"",
        )
    BEGIN_FIRST = (
            "\"BEGIN\"",
            "\"FIRST\"",
        )
    BEGIN_MIDDLE = (
            "\"BEGIN\"",
            "\"MIDDLE\"",
        )
    END = '"END"'
    END_BEGIN = (
            "\"END\"",
            "\"BEGIN\"",
        )
    END_END = (
            "\"END\"",
            "\"END\"",
        )
    END_FIRST = (
            "\"END\"",
            "\"FIRST\"",
        )
    END_MIDDLE = (
            "\"END\"",
            "\"MIDDLE\"",
        )
    FIRST = '"FIRST"'
    FIRST_BEGIN = (
            "\"FIRST\"",
            "\"BEGIN\"",
        )
    FIRST_END = (
            "\"FIRST\"",
            "\"END\"",
        )
    FIRST_FIRST = (
            "\"FIRST\"",
            "\"FIRST\"",
        )
    FIRST_MIDDLE = (
            "\"FIRST\"",
            "\"MIDDLE\"",
        )


class LayoutAlignChoices(Enum):
    LEFT_BOTTOM = (
            "\"LEFT\"",
            "\"BOTTOM\"",
        )
    LEFT_CENTER = (
            "\"LEFT\"",
            "\"CENTER\"",
        )
    LEFT_TOP = (
            "\"LEFT\"",
            "\"TOP\"",
        )
    CENTER_BOTTOM = (
            "\"CENTER\"",
            "\"BOTTOM\"",
        )
    CENTER_CENTER = (
            "\"CENTER\"",
            "\"CENTER\"",
        )
    CENTER_TOP = (
            "\"CENTER\"",
            "\"TOP\"",
        )
    RIGHT_BOTTOM = (
            "\"RIGHT\"",
            "\"BOTTOM\"",
        )
    RIGHT_CENTER = (
            "\"RIGHT\"",
            "\"CENTER\"",
        )
    RIGHT_TOP = (
            "\"RIGHT\"",
            "\"TOP\"",
        )


class LayoutScaleModeChoices(Enum):
    NONE_NONE = (
            "\"NONE\"",
            "\"NONE\"",
        )
    NONE_FRACTION = (
            "\"NONE\"",
            "\"FRACTION\"",
        )
    NONE_STRETCH = (
            "\"NONE\"",
            "\"STRETCH\"",
        )
    NONE_PIXEL = (
            "\"NONE\"",
            "\"PIXEL\"",
        )
    FRACTION_NONE = (
            "\"FRACTION\"",
            "\"NONE\"",
        )
    FRACTION_FRACTION = (
            "\"FRACTION\"",
            "\"FRACTION\"",
        )
    FRACTION_STRETCH = (
            "\"FRACTION\"",
            "\"STRETCH\"",
        )
    FRACTION_PIXEL = (
            "\"FRACTION\"",
            "\"PIXEL\"",
        )
    STRETCH_NONE = (
            "\"STRETCH\"",
            "\"NONE\"",
        )
    STRETCH_FRACTION = (
            "\"STRETCH\"",
            "\"FRACTION\"",
        )
    STRETCH_STRETCH = (
            "\"STRETCH\"",
            "\"STRETCH\"",
        )
    STRETCH_PIXEL = (
            "\"STRETCH\"",
            "\"PIXEL\"",
        )
    PIXEL_NONE = (
            "\"PIXEL\"",
            "\"NONE\"",
        )
    PIXEL_FRACTION = (
            "\"PIXEL\"",
            "\"FRACTION\"",
        )
    PIXEL_STRETCH = (
            "\"PIXEL\"",
            "\"STRETCH\"",
        )
    PIXEL_PIXEL = (
            "\"PIXEL\"",
            "\"PIXEL\"",
        )


class LayoutUnitsChoices(Enum):
    WORLD_WORLD = (
            "\"WORLD\"",
            "\"WORLD\"",
        )
    WORLD_FRACTION = (
            "\"WORLD\"",
            "\"FRACTION\"",
        )
    WORLD_PIXEL = (
            "\"WORLD\"",
            "\"PIXEL\"",
        )
    FRACTION_WORLD = (
            "\"FRACTION\"",
            "\"WORLD\"",
        )
    FRACTION_FRACTION = (
            "\"FRACTION\"",
            "\"FRACTION\"",
        )
    FRACTION_PIXEL = (
            "\"FRACTION\"",
            "\"PIXEL\"",
        )
    PIXEL_WORLD = (
            "\"PIXEL\"",
            "\"WORLD\"",
        )
    PIXEL_FRACTION = (
            "\"PIXEL\"",
            "\"FRACTION\"",
        )
    PIXEL_PIXEL = (
            "\"PIXEL\"",
            "\"PIXEL\"",
        )


class MetaDirectionChoices(Enum):
    RTL = "rtl"
    LTR = "ltr"


class MetaNameValues(Enum):
    ACCESS_RIGHTS = "accessRights"
    AUTHOR = "author"
    CONTRIBUTOR = "contributor"
    CREATED = "created"
    CREATOR = "creator"
    DESCRIPTION = "description"
    DISCLAIMER = "disclaimer"
    DRAWING = "drawing"
    ERROR = "error"
    GENERATOR = "generator"
    HINT = "hint"
    IDENTIFIER = "identifier"
    IMAGE = "Image"
    INFO = "info"
    INFORMATION = "information"
    IS_VERSION_OF = "isVersionOf"
    KEYWORDS = "keywords"
    LICENSE = "license"
    MEDIATOR = "mediator"
    MODIFIED = "modified"
    MOVIE = "movie"
    MOVING_IMAGE = "MovingImage"
    ORIGINAL = "original"
    PHOTO = "photo"
    PHOTOGRAPH = "photograph"
    PUBLISHER = "publisher"
    REFERENCE = "reference"
    REQUIRES = "requires"
    RIGHTS = "rights"
    ROBOTS = "robots"
    SOUND = "Sound"
    SOURCE = "source"
    SPECIFICATION_SECTION = "specificationSection"
    SPECIFICATION_URL = "specificationUrl"
    SUBJECT = "subject"
    TEXT = "Text"
    TITLE = "title"
    TODO = "TODO"
    TRANSLATOR = "translator"
    TRANSLATED = "translated"
    VERSION = "version"
    WARNING = "warning"


class MultiTextureFunctionValues(Enum):
    COMPLEMENT = '"COMPLEMENT"'
    ALPHAREPLICATE = '"ALPHAREPLICATE"'
    VALUE = '""'


class MultiTextureModeValues(Enum):
    ADD = '"ADD"'
    ADDSIGNED = '"ADDSIGNED"'
    ADDSIGNED2_X = '"ADDSIGNED2X"'
    ADDSMOOTH = '"ADDSMOOTH"'
    BLENDCURRENTALPHA = '"BLENDCURRENTALPHA"'
    BLENDDIFFUSEALPHA = '"BLENDDIFFUSEALPHA"'
    BLENDFACTORALPHA = '"BLENDFACTORALPHA"'
    BLENDTEXTUREALPHA = '"BLENDTEXTUREALPHA"'
    DOTPRODUCT3 = '"DOTPRODUCT3"'
    MODULATE = '"MODULATE"'
    MODULATE2_X = '"MODULATE2X"'
    MODULATE4_X = '"MODULATE4X"'
    MODULATEALPHA_ADDCOLOR = '"MODULATEALPHA_ADDCOLOR"'
    MODULATEINVALPHA_ADDCOLOR = '"MODULATEINVALPHA_ADDCOLOR"'
    MODULATEINVCOLOR_ADDALPHA = '"MODULATEINVCOLOR_ADDALPHA"'
    OFF = '"OFF"'
    REPLACE = '"REPLACE"'
    SELECTARG1 = '"SELECTARG1"'
    SELECTARG2 = '"SELECTARG2"'
    SUBTRACT = '"SUBTRACT"'


class MultiTextureSourceValues(Enum):
    DIFFUSE = '"DIFFUSE"'
    FACTOR = '"FACTOR"'
    SPECULAR = '"SPECULAR"'
    VALUE = '""'


class NavigationTransitionTypeValues(Enum):
    TELEPORT = '"TELEPORT"'
    LINEAR = '"LINEAR"'
    ANIMATE = '"ANIMATE"'


class NavigationTypeValues(Enum):
    ANY = '"ANY"'
    WALK = '"WALK"'
    EXAMINE = '"EXAMINE"'
    FLY = '"FLY"'
    LOOKAT = '"LOOKAT"'
    NONE = '"NONE"'
    EXPLORE = '"EXPLORE"'


class NetworkModeChoices(Enum):
    STAND_ALONE = "standAlone"
    NETWORK_READER = "networkReader"
    NETWORK_WRITER = "networkWriter"


class OutputOnlyAccessTypes(Enum):
    ACTION_KEY_PRESS = "actionKeyPress"
    ACTION_KEY_RELEASE = "actionKeyRelease"
    ALT_KEY = "altKey"
    ANGLE = "angle"
    ANGLE_RATE = "angleRate"
    ARTICULATION_PARAMETER_VALUE0_CHANGED = "articulationParameterValue0_changed"
    ARTICULATION_PARAMETER_VALUE1_CHANGED = "articulationParameterValue1_changed"
    ARTICULATION_PARAMETER_VALUE2_CHANGED = "articulationParameterValue2_changed"
    ARTICULATION_PARAMETER_VALUE3_CHANGED = "articulationParameterValue3_changed"
    ARTICULATION_PARAMETER_VALUE4_CHANGED = "articulationParameterValue4_changed"
    ARTICULATION_PARAMETER_VALUE5_CHANGED = "articulationParameterValue5_changed"
    ARTICULATION_PARAMETER_VALUE6_CHANGED = "articulationParameterValue6_changed"
    ARTICULATION_PARAMETER_VALUE7_CHANGED = "articulationParameterValue7_changed"
    BIND_TIME = "bindTime"
    BODY1_ANCHOR_POINT = "body1AnchorPoint"
    BODY1_AXIS = "body1Axis"
    BODY2_ANCHOR_POINT = "body2AnchorPoint"
    BODY2_AXIS = "body2Axis"
    CENTER_OF_ROTATION_CHANGED = "centerOfRotation_changed"
    COLLIDE_TIME = "collideTime"
    CONTROL_KEY = "controlKey"
    CYCLE_TIME = "cycleTime"
    DETONATE_TIME = "detonateTime"
    DURATION_CHANGED = "duration_changed"
    ELAPSED_TIME = "elapsedTime"
    ENTERED_TEXT = "enteredText"
    ENTER_TIME = "enterTime"
    EXIT_TIME = "exitTime"
    FINAL_TEXT = "finalText"
    FIRED_TIME = "firedTime"
    FRACTION_CHANGED = "fraction_changed"
    GEOVALUE_CHANGED = "geovalue_changed"
    HINGE1_ANGLE = "hinge1Angle"
    HINGE1_ANGLE_RATE = "hinge1AngleRate"
    HINGE2_ANGLE = "hinge2Angle"
    HINGE2_ANGLE_RATE = "hinge2AngleRate"
    HIT_GEO_COORD_CHANGED = "hitGeoCoord_changed"
    HIT_NORMAL_CHANGED = "hitNormal_changed"
    HIT_POINT_CHANGED = "hitPoint_changed"
    HIT_TEX_COORD_CHANGED = "hitTexCoord_changed"
    INPUT_FALSE = "inputFalse"
    INPUT_NEGATE = "inputNegate"
    INPUT_TRUE = "inputTrue"
    IS_ACTIVE = "isActive"
    IS_BOUND = "isBound"
    IS_COLLIDED = "isCollided"
    IS_DETONATED = "isDetonated"
    IS_LOADED = "isLoaded"
    IS_OVER = "isOver"
    IS_PAUSED = "isPaused"
    IS_NETWORK_READER = "isNetworkReader"
    IS_NETWORK_WRITER = "isNetworkWriter"
    IS_RTP_HEADER_HEARD = "isRtpHeaderHeard"
    IS_SELECTED = "isSelected"
    IS_STAND_ALONE = "isStandAlone"
    IS_VALID = "isValid"
    KEY_PRESS = "keyPress"
    KEY_RELEASE = "keyRelease"
    LEVEL_CHANGED = "level_changed"
    LINE_BOUNDS = "lineBounds"
    LOAD_TIME = "loadTime"
    MODIFIED_FRACTION_CHANGED = "modifiedFraction_changed"
    MOTOR1_ANGLE = "motor1Angle"
    MOTOR1_ANGLE_RATE = "motor1AngleRate"
    MOTOR2_ANGLE = "motor2Angle"
    MOTOR2_ANGLE_RATE = "motor2AngleRate"
    MOTOR3_ANGLE = "motor3Angle"
    MOTOR3_ANGLE_RATE = "motor3AngleRate"
    NEXT = "next"
    NORMAL_CHANGED = "normal_changed"
    ORIENTATION_CHANGED = "orientation_changed"
    ORIGIN = "origin"
    PICKED_GEOMETRY = "pickedGeometry"
    PICKED_NORMAL = "pickedNormal"
    PICKED_POINT = "pickedPoint"
    PICKED_TEXTURE_COORDINATE = "pickedTextureCoordinate"
    POSITION_CHANGED = "position_changed"
    PREVIOUS = "previous"
    PROGRESS = "progress"
    ROTATION_CHANGED = "rotation_changed"
    SEPARATION = "separation"
    SEPARATION_RATE = "separationRate"
    SHIFT_KEY = "shiftKey"
    TEXT_BOUNDS = "textBounds"
    TIME = "time"
    TIMESTAMP = "timestamp"
    TOUCH_TIME = "touchTime"
    TRACK_POINT_CHANGED = "trackPoint_changed"
    TRANSITION_COMPLETE = "transitionComplete"
    TRANSLATION_CHANGED = "translation_changed"
    TRIGGER_TIME = "triggerTime"
    TRIGGER_TRUE = "triggerTrue"
    TRIGGER_VALUE = "triggerValue"
    VALUE_CHANGED = "value_changed"


class ParticleSystemGeometryTypeValues(Enum):
    LINE = "LINE"
    POINT = "POINT"
    QUAD = "QUAD"
    SPRITE = "SPRITE"
    TRIANGLE = "TRIANGLE"
    GEOMETRY = "GEOMETRY"


class PhaseFunctionValues(Enum):
    HENYEY_GREENSTEIN = "Henyey-Greenstein"
    NONE = "NONE"


class PickSensorMatchCriterionChoices(Enum):
    MATCH_ANY = "MATCH_ANY"
    MATCH_EVERY = "MATCH_EVERY"
    MATCH_ONLY_ONE = "MATCH_ONLY_ONE"


class PickSensorSortOrderValues(Enum):
    ANY = "ANY"
    CLOSEST = "CLOSEST"
    ALL = "ALL"
    ALL_SORTED = "ALL_SORTED"


class PickableObjectTypeValues(Enum):
    ALL = '"ALL"'
    NONE = '"NONE"'
    TERRAIN = '"TERRAIN"'


class ProfileNameChoices(Enum):
    CORE = "Core"
    INTERCHANGE = "Interchange"
    CADINTERCHANGE = "CADInterchange"
    INTERACTIVE = "Interactive"
    IMMERSIVE = "Immersive"
    MEDICAL_INTERCHANGE = "MedicalInterchange"
    MPEG4_INTERACTIVE = "MPEG4Interactive"
    FULL = "Full"


class ProjectionVolumeStyleTypeChoices(Enum):
    MAX = "MAX"
    MIN = "MIN"
    AVERAGE = "AVERAGE"


class ShaderLanguageValues(Enum):
    CG = "Cg"
    GLSL = "GLSL"
    HLSL = "HLSL"


class ShaderPartTypeValues(Enum):
    VERTEX = "VERTEX"
    FRAGMENT = "FRAGMENT"


class TextureBoundaryModeChoices(Enum):
    CLAMP = "CLAMP"
    CLAMP_TO_EDGE = "CLAMP_TO_EDGE"
    CLAMP_TO_BOUNDARY = "CLAMP_TO_BOUNDARY"
    MIRRORED_REPEAT = "MIRRORED_REPEAT"
    REPEAT = "REPEAT"


class TextureCompressionModeChoices(Enum):
    DEFAULT = "DEFAULT"
    FASTEST = "FASTEST"
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    NICEST = "NICEST"


class TextureCoordinateGeneratorModeChoices(Enum):
    SPHERE = "SPHERE"
    CAMERASPACENORMAL = "CAMERASPACENORMAL"
    CAMERASPACEPOSITION = "CAMERASPACEPOSITION"
    CAMERASPACEREFLECTIONVECTOR = "CAMERASPACEREFLECTIONVECTOR"
    SPHERE_LOCAL = "SPHERE-LOCAL"
    COORD = "COORD"
    COORD_EYE = "COORD-EYE"
    NOISE = "NOISE"
    NOISE_EYE = "NOISE-EYE"
    SPHERE_REFLECT = "SPHERE-REFLECT"
    SPHERE_REFLECT_LOCAL = "SPHERE-REFLECT-LOCAL"


class TextureMagnificationModeChoices(Enum):
    AVG_PIXEL = "AVG_PIXEL"
    DEFAULT = "DEFAULT"
    FASTEST = "FASTEST"
    NEAREST_PIXEL = "NEAREST_PIXEL"
    NICEST = "NICEST"


class TextureMinificationModeChoices(Enum):
    AVG_PIXEL = "AVG_PIXEL"
    AVG_PIXEL_AVG_MIPMAP = "AVG_PIXEL_AVG_MIPMAP"
    AVG_PIXEL_NEAREST_MIPMAP = "AVG_PIXEL_NEAREST_MIPMAP"
    DEFAULT = "DEFAULT"
    FASTEST = "FASTEST"
    NEAREST_PIXEL = "NEAREST_PIXEL"
    NEAREST_PIXEL_AVG_MIPMAP = "NEAREST_PIXEL_AVG_MIPMAP"
    NEAREST_PIXEL_NEAREST_MIPMAP = "NEAREST_PIXEL_NEAREST_MIPMAP"
    NICEST = "NICEST"


class UnitCategoryChoices(Enum):
    ANGLE = "angle"
    FORCE = "force"
    LENGTH = "length"
    MASS = "mass"


class VolumeRenderingWeightFunctionChoices(Enum):
    CONSTANT = "CONSTANT"
    ALPHA1 = "ALPHA1"
    ALPHA2 = "ALPHA2"
    ONE_MINUS_ALPHA1 = "ONE_MINUS_ALPHA1"
    ONE_MINUS_ALPHA2 = "ONE_MINUS_ALPHA2"
    TABLE = "TABLE"


class X3DVersionChoices(Enum):
    VALUE_3_0 = "3.0"
    VALUE_3_1 = "3.1"
    VALUE_3_2 = "3.2"
    VALUE_3_3 = "3.3"


@dataclass
class Export(SceneGraphStructureStatement):
    class Meta:
        name = "EXPORT"
        namespace = "http://www.design2machine.com"

    local_def: Optional[str] = field(
        default=None,
        metadata={
            "name": "localDEF",
            "type": "Attribute",
            "required": True,
        }
    )
    as_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "AS",
            "type": "Attribute",
        }
    )


@dataclass
class ExternProtoDeclare(SceneGraphStructureStatement):
    class Meta:
        namespace = "http://www.design2machine.com"

    field_value: List["Field"] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    appinfo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Import(SceneGraphStructureStatement):
    class Meta:
        name = "IMPORT"
        namespace = "http://www.design2machine.com"

    inline_def: Optional[str] = field(
        default=None,
        metadata={
            "name": "inlineDEF",
            "type": "Attribute",
            "required": True,
        }
    )
    imported_def: Optional[str] = field(
        default=None,
        metadata={
            "name": "importedDEF",
            "type": "Attribute",
            "required": True,
        }
    )
    as_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "AS",
            "type": "Attribute",
        }
    )


@dataclass
class ProtoInterface(SceneGraphStructureStatement):
    class Meta:
        namespace = "http://www.design2machine.com"

    field_value: List["Field"] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )


@dataclass
class Route(SceneGraphStructureStatement):
    class Meta:
        name = "ROUTE"
        namespace = "http://www.design2machine.com"

    from_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "fromNode",
            "type": "Attribute",
            "required": True,
        }
    )
    from_field: Optional[str] = field(
        default=None,
        metadata={
            "name": "fromField",
            "type": "Attribute",
            "required": True,
        }
    )
    to_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "toNode",
            "type": "Attribute",
            "required": True,
        }
    )
    to_field: Optional[str] = field(
        default=None,
        metadata={
            "name": "toField",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class X3DfogObject:
    class Meta:
        name = "X3DFogObject"

    color: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    fog_type: FogTypeChoices = field(
        default=FogTypeChoices.LINEAR,
        metadata={
            "name": "fogType",
            "type": "Attribute",
        }
    )
    visibility_range: float = field(
        default=0.0,
        metadata={
            "name": "visibilityRange",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )


@dataclass
class Component(SceneGraphStructureStatement):
    class Meta:
        name = "component"
        namespace = "http://www.design2machine.com"

    name: Optional[ComponentNameChoices] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    level: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )


@dataclass
class Connect(SceneGraphStructureStatement):
    class Meta:
        name = "connect"
        namespace = "http://www.design2machine.com"

    node_field: Optional[str] = field(
        default=None,
        metadata={
            "name": "nodeField",
            "type": "Attribute",
            "required": True,
        }
    )
    proto_field: Optional[str] = field(
        default=None,
        metadata={
            "name": "protoField",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MetaType(SceneGraphStructureStatement):
    class Meta:
        name = "meta"
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    dir: Optional[MetaDirectionChoices] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    http_equiv: Optional[str] = field(
        default=None,
        metadata={
            "name": "http-equiv",
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Unit(SceneGraphStructureStatement):
    class Meta:
        name = "unit"
        namespace = "http://www.design2machine.com"

    category: Optional[UnitCategoryChoices] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    conversion_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "conversionFactor",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        }
    )


@dataclass
class Is(SceneGraphStructureStatement):
    class Meta:
        name = "IS"
        namespace = "http://www.design2machine.com"

    connect: List[Connect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Head(SceneGraphStructureStatement):
    class Meta:
        name = "head"
        namespace = "http://www.design2machine.com"

    component: List[Component] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unit: List[Unit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    meta: List[MetaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PackagedShader:
    class Meta:
        namespace = "http://www.design2machine.com"

    field_value: List["Field"] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesPackagedShader = field(
        default=ContainerFieldChoicesPackagedShader.SHADERS,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ShaderPart(X3DnodeMixedContent):
    """
    :ivar is_value:
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar type:
    :ivar url:
    :ivar container_field: parent ComposedShader node
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    type: str = field(
        default="VERTEX",
        metadata={
            "type": "Attribute",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesShaderPart = field(
        default=ContainerFieldChoicesShaderPart.PARTS,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ShaderProgram(X3DnodeMixedContent):
    class Meta:
        namespace = "http://www.design2machine.com"

    field_value: List["Field"] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    type: str = field(
        default="VERTEX",
        metadata={
            "type": "Attribute",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: str = field(
        default="programs",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3DscriptNode:
    class Meta:
        name = "X3DScriptNode"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    field_value: List["Field"] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Script(X3DscriptNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    direct_output: bool = field(
        default=False,
        metadata={
            "name": "directOutput",
            "type": "Attribute",
        }
    )
    must_evaluate: bool = field(
        default=False,
        metadata={
            "name": "mustEvaluate",
            "type": "Attribute",
        }
    )
    container_field: ContainerFieldChoicesX3DurlObject = field(
        default=ContainerFieldChoicesX3DurlObject.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ProtoBody(SceneGraphStructureStatement):
    """
    :ivar fill_properties: fillProperties
    :ivar line_properties: lineProperties
    :ivar material: material
    :ivar two_sided_material: material
    :ivar composed_shader: shaders
    :ivar packaged_shader: shaders
    :ivar program_shader: shaders
    :ivar composed_cube_map_texture: texture
    :ivar composed_texture3_d: texture
    :ivar image_texture: texture
    :ivar image_texture3_d: texture
    :ivar movie_texture: texture
    :ivar multi_texture: texture
    :ivar pixel_texture: texture
    :ivar pixel_texture3_d: texture
    :ivar generated_cube_map_texture: texture
    :ivar image_cube_map_texture: texture
    :ivar multi_texture_transform: textureTransform
    :ivar texture_transform: textureTransform
    :ivar texture_transform3_d: textureTransform
    :ivar texture_transform_matrix3_d: textureTransform
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar appearance:
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar font_style:
    :ivar screen_font_style:
    :ivar geo_coordinate:
    :ivar normal:
    :ivar texture_coordinate:
    :ivar contour2_d:
    :ivar contour_polyline2_d:
    :ivar nurbs_texture_coordinate:
    :ivar layer:
    :ivar layout_layer:
    :ivar viewport:
    :ivar ball_joint:
    :ivar collidable_offset:
    :ivar collision_collection:
    :ivar collision_space:
    :ivar contact:
    :ivar double_axis_hinge_joint:
    :ivar motor_joint:
    :ivar rigid_body:
    :ivar single_axis_hinge_joint:
    :ivar slider_joint:
    :ivar universal_joint:
    :ivar route:
    :ivar extern_proto_declare:
    :ivar proto_declare:
    :ivar import_value:
    :ivar export:
    :ivar geo_origin:
    :ivar layer_set: At most one LayerSet can appear in a scene and must
        be a root node.
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    fill_properties: List["FillProperties"] = field(
        default_factory=list,
        metadata={
            "name": "FillProperties",
            "type": "Element",
        }
    )
    line_properties: List["LineProperties"] = field(
        default_factory=list,
        metadata={
            "name": "LineProperties",
            "type": "Element",
        }
    )
    material: List["Material"] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
        }
    )
    two_sided_material: List["TwoSidedMaterial"] = field(
        default_factory=list,
        metadata={
            "name": "TwoSidedMaterial",
            "type": "Element",
        }
    )
    composed_shader: List["ComposedShader"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedShader",
            "type": "Element",
        }
    )
    packaged_shader: List[PackagedShader] = field(
        default_factory=list,
        metadata={
            "name": "PackagedShader",
            "type": "Element",
        }
    )
    program_shader: List["ProgramShader"] = field(
        default_factory=list,
        metadata={
            "name": "ProgramShader",
            "type": "Element",
        }
    )
    composed_cube_map_texture: List["ComposedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedCubeMapTexture",
            "type": "Element",
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    multi_texture: List["MultiTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    generated_cube_map_texture: List["GeneratedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "GeneratedCubeMapTexture",
            "type": "Element",
        }
    )
    image_cube_map_texture: List["ImageCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageCubeMapTexture",
            "type": "Element",
        }
    )
    multi_texture_transform: List["MultiTextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureTransform",
            "type": "Element",
        }
    )
    texture_transform: List["TextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform",
            "type": "Element",
        }
    )
    texture_transform3_d: List["TextureTransform3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform3D",
            "type": "Element",
        }
    )
    texture_transform_matrix3_d: List["TextureTransformMatrix3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransformMatrix3D",
            "type": "Element",
        }
    )
    metadata_boolean: List["MetadataBoolean"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: List["MetadataDouble"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: List["MetadataFloat"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: List["MetadataInteger"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: List["MetadataSet"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: List["MetadataString"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    box: List["Box"] = field(
        default_factory=list,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: List["Cone"] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: List["Cylinder"] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: List["IndexedFaceSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: List["IndexedLineSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: List["IndexedTriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: List["IndexedTriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: List["IndexedTriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: List["LineSet"] = field(
        default_factory=list,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: List["PointSet"] = field(
        default_factory=list,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: List["Sphere"] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: List["TriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: List["TriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: List["TriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: List["ElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: List["Polyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: List["Polypoint2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: List["Rectangle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: List["TriangleSet2D"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: List["Extrusion"] = field(
        default_factory=list,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: List["Text"] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: List["Arc2D"] = field(
        default_factory=list,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: List["ArcClose2D"] = field(
        default_factory=list,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: List["Circle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: List["Disk2D"] = field(
        default_factory=list,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: List["QuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: List["IndexedQuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: List["GeoElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: List["NurbsCurve"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    appearance: List["Appearance"] = field(
        default_factory=list,
        metadata={
            "name": "Appearance",
            "type": "Element",
        }
    )
    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    font_style: List["FontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "FontStyle",
            "type": "Element",
        }
    )
    screen_font_style: List["ScreenFontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenFontStyle",
            "type": "Element",
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    contour2_d: List["Contour2D"] = field(
        default_factory=list,
        metadata={
            "name": "Contour2D",
            "type": "Element",
        }
    )
    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
        }
    )
    layer: List["Layer"] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
        }
    )
    layout_layer: List["LayoutLayer"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutLayer",
            "type": "Element",
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
        }
    )
    ball_joint: List["BallJoint"] = field(
        default_factory=list,
        metadata={
            "name": "BallJoint",
            "type": "Element",
        }
    )
    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collision_collection: List["CollisionCollection"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionCollection",
            "type": "Element",
        }
    )
    collision_space: List["CollisionSpace"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSpace",
            "type": "Element",
        }
    )
    contact: List["Contact"] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        }
    )
    double_axis_hinge_joint: List["DoubleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "DoubleAxisHingeJoint",
            "type": "Element",
        }
    )
    motor_joint: List["MotorJoint"] = field(
        default_factory=list,
        metadata={
            "name": "MotorJoint",
            "type": "Element",
        }
    )
    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
        }
    )
    single_axis_hinge_joint: List["SingleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SingleAxisHingeJoint",
            "type": "Element",
        }
    )
    slider_joint: List["SliderJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SliderJoint",
            "type": "Element",
        }
    )
    universal_joint: List["UniversalJoint"] = field(
        default_factory=list,
        metadata={
            "name": "UniversalJoint",
            "type": "Element",
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "ROUTE",
            "type": "Element",
        }
    )
    extern_proto_declare: List[ExternProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ExternProtoDeclare",
            "type": "Element",
        }
    )
    proto_declare: List["ProtoDeclare"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoDeclare",
            "type": "Element",
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "IMPORT",
            "type": "Element",
        }
    )
    export: List[Export] = field(
        default_factory=list,
        metadata={
            "name": "EXPORT",
            "type": "Element",
        }
    )
    geo_origin: List["GeoOrigin"] = field(
        default_factory=list,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    layer_set: List["LayerSet"] = field(
        default_factory=list,
        metadata={
            "name": "LayerSet",
            "type": "Element",
        }
    )


@dataclass
class Field(SceneGraphStructureStatement):
    """
    :ivar fill_properties: fillProperties
    :ivar line_properties: lineProperties
    :ivar material: material
    :ivar two_sided_material: material
    :ivar composed_shader: shaders
    :ivar packaged_shader: shaders
    :ivar program_shader: shaders
    :ivar composed_cube_map_texture: texture
    :ivar composed_texture3_d: texture
    :ivar image_texture: texture
    :ivar image_texture3_d: texture
    :ivar movie_texture: texture
    :ivar multi_texture: texture
    :ivar pixel_texture: texture
    :ivar pixel_texture3_d: texture
    :ivar generated_cube_map_texture: texture
    :ivar image_cube_map_texture: texture
    :ivar multi_texture_transform: textureTransform
    :ivar texture_transform: textureTransform
    :ivar texture_transform3_d: textureTransform
    :ivar texture_transform_matrix3_d: textureTransform
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar appearance:
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar font_style:
    :ivar screen_font_style:
    :ivar geo_coordinate:
    :ivar normal:
    :ivar texture_coordinate:
    :ivar contour2_d:
    :ivar contour_polyline2_d:
    :ivar nurbs_texture_coordinate:
    :ivar layer:
    :ivar layout_layer:
    :ivar viewport:
    :ivar ball_joint:
    :ivar collidable_offset:
    :ivar collision_collection:
    :ivar collision_space:
    :ivar contact:
    :ivar double_axis_hinge_joint:
    :ivar motor_joint:
    :ivar rigid_body:
    :ivar single_axis_hinge_joint:
    :ivar slider_joint:
    :ivar universal_joint:
    :ivar name:
    :ivar access_type:
    :ivar type:
    :ivar value:
    :ivar appinfo:
    :ivar documentation:
    """
    class Meta:
        name = "field"
        namespace = "http://www.design2machine.com"

    fill_properties: List["FillProperties"] = field(
        default_factory=list,
        metadata={
            "name": "FillProperties",
            "type": "Element",
        }
    )
    line_properties: List["LineProperties"] = field(
        default_factory=list,
        metadata={
            "name": "LineProperties",
            "type": "Element",
        }
    )
    material: List["Material"] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
        }
    )
    two_sided_material: List["TwoSidedMaterial"] = field(
        default_factory=list,
        metadata={
            "name": "TwoSidedMaterial",
            "type": "Element",
        }
    )
    composed_shader: List["ComposedShader"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedShader",
            "type": "Element",
        }
    )
    packaged_shader: List[PackagedShader] = field(
        default_factory=list,
        metadata={
            "name": "PackagedShader",
            "type": "Element",
        }
    )
    program_shader: List["ProgramShader"] = field(
        default_factory=list,
        metadata={
            "name": "ProgramShader",
            "type": "Element",
        }
    )
    composed_cube_map_texture: List["ComposedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedCubeMapTexture",
            "type": "Element",
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    multi_texture: List["MultiTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    generated_cube_map_texture: List["GeneratedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "GeneratedCubeMapTexture",
            "type": "Element",
        }
    )
    image_cube_map_texture: List["ImageCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageCubeMapTexture",
            "type": "Element",
        }
    )
    multi_texture_transform: List["MultiTextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureTransform",
            "type": "Element",
        }
    )
    texture_transform: List["TextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform",
            "type": "Element",
        }
    )
    texture_transform3_d: List["TextureTransform3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform3D",
            "type": "Element",
        }
    )
    texture_transform_matrix3_d: List["TextureTransformMatrix3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransformMatrix3D",
            "type": "Element",
        }
    )
    metadata_boolean: List["MetadataBoolean"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: List["MetadataDouble"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: List["MetadataFloat"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: List["MetadataInteger"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: List["MetadataSet"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: List["MetadataString"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    box: List["Box"] = field(
        default_factory=list,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: List["Cone"] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: List["Cylinder"] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: List["IndexedFaceSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: List["IndexedLineSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: List["IndexedTriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: List["IndexedTriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: List["IndexedTriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: List["LineSet"] = field(
        default_factory=list,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: List["PointSet"] = field(
        default_factory=list,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: List["Sphere"] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: List["TriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: List["TriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: List["TriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: List["ElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: List["Polyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: List["Polypoint2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: List["Rectangle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: List["TriangleSet2D"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: List["Extrusion"] = field(
        default_factory=list,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: List["Text"] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: List["Arc2D"] = field(
        default_factory=list,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: List["ArcClose2D"] = field(
        default_factory=list,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: List["Circle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: List["Disk2D"] = field(
        default_factory=list,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: List["QuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: List["IndexedQuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: List["GeoElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: List["NurbsCurve"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    appearance: List["Appearance"] = field(
        default_factory=list,
        metadata={
            "name": "Appearance",
            "type": "Element",
        }
    )
    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    font_style: List["FontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "FontStyle",
            "type": "Element",
        }
    )
    screen_font_style: List["ScreenFontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenFontStyle",
            "type": "Element",
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    contour2_d: List["Contour2D"] = field(
        default_factory=list,
        metadata={
            "name": "Contour2D",
            "type": "Element",
        }
    )
    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
        }
    )
    layer: List["Layer"] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
        }
    )
    layout_layer: List["LayoutLayer"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutLayer",
            "type": "Element",
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
        }
    )
    ball_joint: List["BallJoint"] = field(
        default_factory=list,
        metadata={
            "name": "BallJoint",
            "type": "Element",
        }
    )
    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collision_collection: List["CollisionCollection"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionCollection",
            "type": "Element",
        }
    )
    collision_space: List["CollisionSpace"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSpace",
            "type": "Element",
        }
    )
    contact: List["Contact"] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        }
    )
    double_axis_hinge_joint: List["DoubleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "DoubleAxisHingeJoint",
            "type": "Element",
        }
    )
    motor_joint: List["MotorJoint"] = field(
        default_factory=list,
        metadata={
            "name": "MotorJoint",
            "type": "Element",
        }
    )
    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
        }
    )
    single_axis_hinge_joint: List["SingleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SingleAxisHingeJoint",
            "type": "Element",
        }
    )
    slider_joint: List["SliderJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SliderJoint",
            "type": "Element",
        }
    )
    universal_joint: List["UniversalJoint"] = field(
        default_factory=list,
        metadata={
            "name": "UniversalJoint",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    access_type: Optional[AccessTypeChoices] = field(
        default=None,
        metadata={
            "name": "accessType",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    appinfo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ComposedShader:
    """
    :ivar field_value:
    :ivar is_value:
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar shader_part:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar def_value:
    :ivar use:
    :ivar class_value:
    :ivar language:
    :ivar container_field: parent Appearance node
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    shader_part: List[ShaderPart] = field(
        default_factory=list,
        metadata={
            "name": "ShaderPart",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="shaders",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ProtoDeclare(SceneGraphStructureStatement):
    class Meta:
        namespace = "http://www.design2machine.com"

    proto_interface: Optional[ProtoInterface] = field(
        default=None,
        metadata={
            "name": "ProtoInterface",
            "type": "Element",
        }
    )
    proto_body: Optional[ProtoBody] = field(
        default=None,
        metadata={
            "name": "ProtoBody",
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    appinfo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FieldValue(SceneGraphStructureStatement):
    """
    :ivar fill_properties: fillProperties
    :ivar line_properties: lineProperties
    :ivar material: material
    :ivar two_sided_material: material
    :ivar composed_shader: shaders
    :ivar packaged_shader: shaders
    :ivar program_shader: shaders
    :ivar composed_cube_map_texture: texture
    :ivar composed_texture3_d: texture
    :ivar image_texture: texture
    :ivar image_texture3_d: texture
    :ivar movie_texture: texture
    :ivar multi_texture: texture
    :ivar pixel_texture: texture
    :ivar pixel_texture3_d: texture
    :ivar generated_cube_map_texture: texture
    :ivar image_cube_map_texture: texture
    :ivar multi_texture_transform: textureTransform
    :ivar texture_transform: textureTransform
    :ivar texture_transform3_d: textureTransform
    :ivar texture_transform_matrix3_d: textureTransform
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar appearance:
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar font_style:
    :ivar screen_font_style:
    :ivar geo_coordinate:
    :ivar normal:
    :ivar texture_coordinate:
    :ivar contour2_d:
    :ivar contour_polyline2_d:
    :ivar nurbs_texture_coordinate:
    :ivar layer:
    :ivar layout_layer:
    :ivar viewport:
    :ivar ball_joint:
    :ivar collidable_offset:
    :ivar collision_collection:
    :ivar collision_space:
    :ivar contact:
    :ivar double_axis_hinge_joint:
    :ivar motor_joint:
    :ivar rigid_body:
    :ivar single_axis_hinge_joint:
    :ivar slider_joint:
    :ivar universal_joint:
    :ivar name:
    :ivar value:
    """
    class Meta:
        name = "fieldValue"
        namespace = "http://www.design2machine.com"

    fill_properties: List["FillProperties"] = field(
        default_factory=list,
        metadata={
            "name": "FillProperties",
            "type": "Element",
        }
    )
    line_properties: List["LineProperties"] = field(
        default_factory=list,
        metadata={
            "name": "LineProperties",
            "type": "Element",
        }
    )
    material: List["Material"] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
        }
    )
    two_sided_material: List["TwoSidedMaterial"] = field(
        default_factory=list,
        metadata={
            "name": "TwoSidedMaterial",
            "type": "Element",
        }
    )
    composed_shader: List[ComposedShader] = field(
        default_factory=list,
        metadata={
            "name": "ComposedShader",
            "type": "Element",
        }
    )
    packaged_shader: List[PackagedShader] = field(
        default_factory=list,
        metadata={
            "name": "PackagedShader",
            "type": "Element",
        }
    )
    program_shader: List["ProgramShader"] = field(
        default_factory=list,
        metadata={
            "name": "ProgramShader",
            "type": "Element",
        }
    )
    composed_cube_map_texture: List["ComposedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedCubeMapTexture",
            "type": "Element",
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    multi_texture: List["MultiTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    generated_cube_map_texture: List["GeneratedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "GeneratedCubeMapTexture",
            "type": "Element",
        }
    )
    image_cube_map_texture: List["ImageCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageCubeMapTexture",
            "type": "Element",
        }
    )
    multi_texture_transform: List["MultiTextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureTransform",
            "type": "Element",
        }
    )
    texture_transform: List["TextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform",
            "type": "Element",
        }
    )
    texture_transform3_d: List["TextureTransform3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform3D",
            "type": "Element",
        }
    )
    texture_transform_matrix3_d: List["TextureTransformMatrix3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransformMatrix3D",
            "type": "Element",
        }
    )
    metadata_boolean: List["MetadataBoolean"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: List["MetadataDouble"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: List["MetadataFloat"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: List["MetadataInteger"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: List["MetadataSet"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: List["MetadataString"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    box: List["Box"] = field(
        default_factory=list,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: List["Cone"] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: List["Cylinder"] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: List["IndexedFaceSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: List["IndexedLineSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: List["IndexedTriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: List["IndexedTriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: List["IndexedTriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: List["LineSet"] = field(
        default_factory=list,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: List["PointSet"] = field(
        default_factory=list,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: List["Sphere"] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: List["TriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: List["TriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: List["TriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: List["ElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: List["Polyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: List["Polypoint2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: List["Rectangle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: List["TriangleSet2D"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: List["Extrusion"] = field(
        default_factory=list,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: List["Text"] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: List["Arc2D"] = field(
        default_factory=list,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: List["ArcClose2D"] = field(
        default_factory=list,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: List["Circle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: List["Disk2D"] = field(
        default_factory=list,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: List["QuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: List["IndexedQuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: List["GeoElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: List["NurbsCurve"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    appearance: List["Appearance"] = field(
        default_factory=list,
        metadata={
            "name": "Appearance",
            "type": "Element",
        }
    )
    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    font_style: List["FontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "FontStyle",
            "type": "Element",
        }
    )
    screen_font_style: List["ScreenFontStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenFontStyle",
            "type": "Element",
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    contour2_d: List["Contour2D"] = field(
        default_factory=list,
        metadata={
            "name": "Contour2D",
            "type": "Element",
        }
    )
    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
        }
    )
    layer: List["Layer"] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
        }
    )
    layout_layer: List["LayoutLayer"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutLayer",
            "type": "Element",
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
        }
    )
    ball_joint: List["BallJoint"] = field(
        default_factory=list,
        metadata={
            "name": "BallJoint",
            "type": "Element",
        }
    )
    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collision_collection: List["CollisionCollection"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionCollection",
            "type": "Element",
        }
    )
    collision_space: List["CollisionSpace"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSpace",
            "type": "Element",
        }
    )
    contact: List["Contact"] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        }
    )
    double_axis_hinge_joint: List["DoubleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "DoubleAxisHingeJoint",
            "type": "Element",
        }
    )
    motor_joint: List["MotorJoint"] = field(
        default_factory=list,
        metadata={
            "name": "MotorJoint",
            "type": "Element",
        }
    )
    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
        }
    )
    single_axis_hinge_joint: List["SingleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SingleAxisHingeJoint",
            "type": "Element",
        }
    )
    slider_joint: List["SliderJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SliderJoint",
            "type": "Element",
        }
    )
    universal_joint: List["UniversalJoint"] = field(
        default_factory=list,
        metadata={
            "name": "UniversalJoint",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DprototypeInstance:
    class Meta:
        name = "X3DPrototypeInstance"

    field_value: List[FieldValue] = field(
        default_factory=list,
        metadata={
            "name": "fieldValue",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_set: Optional["MetadataSet"] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class ProtoInstance(X3DprototypeInstance):
    class Meta:
        namespace = "http://www.design2machine.com"

    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataSet:
    class Meta:
        namespace = "http://www.design2machine.com"

    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_boolean: List["MetadataBoolean"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata_double: List["MetadataDouble"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata_float: List["MetadataFloat"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata_integer: List["MetadataInteger"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata_set: List["MetadataSet"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata_string: List["MetadataString"] = field(
        default_factory=list,
        metadata={
            "name": "MetadataString",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List[ProtoInstance] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3Dnode:
    class Meta:
        name = "X3DNode"

    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_boolean: Optional["MetadataBoolean"] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_double: Optional["MetadataDouble"] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_float: Optional["MetadataFloat"] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_integer: Optional["MetadataInteger"] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_set: Optional[MetadataSet] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_string: Optional["MetadataString"] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Contact(X3Dnode):
    """
    :ivar rigid_body: body1
    :ivar collidable_offset:
    :ivar collidable_shape:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar applied_parameters: array of appliedParametersChoices. Note
        that strict validation of appliedParameters enumeration values
        does not occur via schema since MFString allows any value in any
        order.
    :ivar bounce:
    :ivar contact_normal:
    :ivar depth:
    :ivar friction_coefficients:
    :ivar friction_direction:
    :ivar min_bounce_speed:
    :ivar position:
    :ivar slip_coefficients:
    :ivar softness_constant_force_mix:
    :ivar softness_error_correction:
    :ivar surface_speed:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    applied_parameters: List[str] = field(
        default_factory=lambda: [
            "\"BOUNCE\"",
        ],
        metadata={
            "name": "appliedParameters",
            "type": "Attribute",
            "tokens": True,
        }
    )
    bounce: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    contact_normal: str = field(
        default="0 1 0",
        metadata={
            "name": "contactNormal",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    depth: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    friction_coefficients: str = field(
        default="0 0",
        metadata={
            "name": "frictionCoefficients",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    friction_direction: str = field(
        default="0 1 0",
        metadata={
            "name": "frictionDirection",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    min_bounce_speed: float = field(
        default=0.0,
        metadata={
            "name": "minBounceSpeed",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    position: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    slip_coefficients: str = field(
        default="0 0",
        metadata={
            "name": "slipCoefficients",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    softness_constant_force_mix: float = field(
        default=0.0001,
        metadata={
            "name": "softnessConstantForceMix",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    softness_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "softnessErrorCorrection",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    surface_speed: str = field(
        default="0 0",
        metadata={
            "name": "surfaceSpeed",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="contacts",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Contour2D(X3Dnode):
    """
    :ivar nurbs_curve2_d:
    :ivar contour_polyline2_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    nurbs_curve2_d: List["NurbsCurve2D"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve2D",
            "type": "Element",
        }
    )
    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="trimmingContour",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoOrigin(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotate_yup: bool = field(
        default=False,
        metadata={
            "name": "rotateYUp",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geoOrigin",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LayerSet(X3Dnode):
    """
    :ivar layer:
    :ivar layout_layer:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar active_layer:
    :ivar order:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    layer: List["Layer"] = field(
        default_factory=list,
        metadata={
            "name": "Layer",
            "type": "Element",
        }
    )
    layout_layer: List["LayoutLayer"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutLayer",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    active_layer: int = field(
        default=0,
        metadata={
            "name": "activeLayer",
            "type": "Attribute",
        }
    )
    order: str = field(
        default="0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LayoutGroup(X3Dnode):
    """
    :ivar layout: layout
    :ivar viewport: viewport
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    layout: List["Layout"] = field(
        default_factory=list,
        metadata={
            "name": "Layout",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataBoolean(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataDouble(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataFloat(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataInteger(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MetadataString(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesMetadata = field(
        default=ContainerFieldChoicesMetadata.METADATA,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsTextureCoordinate(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    control_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    u_dimension: int = field(
        default=0,
        metadata={
            "name": "uDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    v_dimension: int = field(
        default=0,
        metadata={
            "name": "vDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    u_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "uKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    v_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "vKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    u_order: int = field(
        default=3,
        metadata={
            "name": "uOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    v_order: int = field(
        default=3,
        metadata={
            "name": "vOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="texCoord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class RigidBody(X3Dnode):
    """
    :ivar sphere: massDensityModel
    :ivar box: massDensityModel
    :ivar cone: massDensityModel
    :ivar collidable_offset: geometry
    :ivar collidable_shape: geometry
    :ivar proto_instance: Appropriately typed substitution node
    :ivar angular_damping_factor:
    :ivar angular_velocity:
    :ivar auto_damp:
    :ivar auto_disable:
    :ivar center_of_mass:
    :ivar disable_angular_speed:
    :ivar disable_linear_speed:
    :ivar disable_time:
    :ivar enabled:
    :ivar finite_rotation_axis:
    :ivar fixed:
    :ivar forces:
    :ivar inertia:
    :ivar linear_damping_factor:
    :ivar linear_velocity:
    :ivar mass:
    :ivar position:
    :ivar orientation:
    :ivar torques:
    :ivar use_finite_rotation:
    :ivar use_global_gravity:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    sphere: List["Sphere"] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    box: List["Box"] = field(
        default_factory=list,
        metadata={
            "name": "Box",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    cone: List["Cone"] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
            "sequential": True,
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    angular_damping_factor: float = field(
        default=0.001,
        metadata={
            "name": "angularDampingFactor",
            "type": "Attribute",
        }
    )
    angular_velocity: str = field(
        default="0 0 0",
        metadata={
            "name": "angularVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    auto_damp: bool = field(
        default=False,
        metadata={
            "name": "autoDamp",
            "type": "Attribute",
        }
    )
    auto_disable: bool = field(
        default=False,
        metadata={
            "name": "autoDisable",
            "type": "Attribute",
        }
    )
    center_of_mass: str = field(
        default="0 0 0",
        metadata={
            "name": "centerOfMass",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    disable_angular_speed: float = field(
        default=0.0,
        metadata={
            "name": "disableAngularSpeed",
            "type": "Attribute",
        }
    )
    disable_linear_speed: float = field(
        default=0.0,
        metadata={
            "name": "disableLinearSpeed",
            "type": "Attribute",
        }
    )
    disable_time: float = field(
        default=0.0,
        metadata={
            "name": "disableTime",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    finite_rotation_axis: str = field(
        default="0 1 0",
        metadata={
            "name": "finiteRotationAxis",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    forces: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    inertia: str = field(
        default="1 0 0 0 1 0 0 0 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){8}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    linear_damping_factor: float = field(
        default=0.001,
        metadata={
            "name": "linearDampingFactor",
            "type": "Attribute",
        }
    )
    linear_velocity: str = field(
        default="0 0 0",
        metadata={
            "name": "linearVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    mass: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        }
    )
    position: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    orientation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    torques: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    use_finite_rotation: bool = field(
        default=False,
        metadata={
            "name": "useFiniteRotation",
            "type": "Attribute",
        }
    )
    use_global_gravity: bool = field(
        default=True,
        metadata={
            "name": "useGlobalGravity",
            "type": "Attribute",
        }
    )
    container_field: RigidBodyContainerField = field(
        default=RigidBodyContainerField.BODIES,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureProperties(X3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anisotropic_degree: float = field(
        default=1.0,
        metadata={
            "name": "anisotropicDegree",
            "type": "Attribute",
            "min_inclusive": 1.0,
        }
    )
    border_color: str = field(
        default="0 0 0 0",
        metadata={
            "name": "borderColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    border_width: int = field(
        default=0,
        metadata={
            "name": "borderWidth",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    boundary_mode_s: TextureBoundaryModeChoices = field(
        default=TextureBoundaryModeChoices.REPEAT,
        metadata={
            "name": "boundaryModeS",
            "type": "Attribute",
        }
    )
    boundary_mode_t: TextureBoundaryModeChoices = field(
        default=TextureBoundaryModeChoices.REPEAT,
        metadata={
            "name": "boundaryModeT",
            "type": "Attribute",
        }
    )
    boundary_mode_r: TextureBoundaryModeChoices = field(
        default=TextureBoundaryModeChoices.REPEAT,
        metadata={
            "name": "boundaryModeR",
            "type": "Attribute",
        }
    )
    magnification_filter: TextureMagnificationModeChoices = field(
        default=TextureMagnificationModeChoices.FASTEST,
        metadata={
            "name": "magnificationFilter",
            "type": "Attribute",
        }
    )
    minification_filter: TextureMinificationModeChoices = field(
        default=TextureMinificationModeChoices.FASTEST,
        metadata={
            "name": "minificationFilter",
            "type": "Attribute",
        }
    )
    texture_compression: TextureCompressionModeChoices = field(
        default=TextureCompressionModeChoices.FASTEST,
        metadata={
            "name": "textureCompression",
            "type": "Attribute",
        }
    )
    texture_priority: float = field(
        default=0.0,
        metadata={
            "name": "texturePriority",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    generate_mip_maps: bool = field(
        default=False,
        metadata={
            "name": "generateMipMaps",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="textureProperties",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3DappearanceChildNode(X3Dnode):
    class Meta:
        name = "X3DAppearanceChildNode"


@dataclass
class X3DappearanceNode(X3Dnode):
    """
    :ivar fill_properties: fillProperties
    :ivar line_properties: lineProperties
    :ivar material: material
    :ivar two_sided_material: material
    :ivar composed_shader: shaders
    :ivar packaged_shader: shaders
    :ivar program_shader: shaders
    :ivar composed_cube_map_texture: texture
    :ivar composed_texture3_d: texture
    :ivar image_texture: texture
    :ivar image_texture3_d: texture
    :ivar movie_texture: texture
    :ivar multi_texture: texture
    :ivar pixel_texture: texture
    :ivar pixel_texture3_d: texture
    :ivar generated_cube_map_texture: texture
    :ivar image_cube_map_texture: texture
    :ivar multi_texture_transform: textureTransform
    :ivar texture_transform: textureTransform
    :ivar texture_transform3_d: textureTransform
    :ivar texture_transform_matrix3_d: textureTransform
    :ivar proto_instance: Appropriately typed substitution node
    """
    class Meta:
        name = "X3DAppearanceNode"

    fill_properties: List["FillProperties"] = field(
        default_factory=list,
        metadata={
            "name": "FillProperties",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    line_properties: List["LineProperties"] = field(
        default_factory=list,
        metadata={
            "name": "LineProperties",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    material: List["Material"] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    two_sided_material: List["TwoSidedMaterial"] = field(
        default_factory=list,
        metadata={
            "name": "TwoSidedMaterial",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    composed_shader: List["ComposedShader"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedShader",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    packaged_shader: List[PackagedShader] = field(
        default_factory=list,
        metadata={
            "name": "PackagedShader",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    program_shader: List["ProgramShader"] = field(
        default_factory=list,
        metadata={
            "name": "ProgramShader",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    composed_cube_map_texture: List["ComposedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedCubeMapTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    multi_texture: List["MultiTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    generated_cube_map_texture: List["GeneratedCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "GeneratedCubeMapTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    image_cube_map_texture: List["ImageCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageCubeMapTexture",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    multi_texture_transform: List["MultiTextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureTransform",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_transform: List["TextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_transform3_d: List["TextureTransform3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_transform_matrix3_d: List["TextureTransformMatrix3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransformMatrix3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class X3DchildNode(X3Dnode):
    class Meta:
        name = "X3DChildNode"


@dataclass
class X3DfontStyleNode(X3Dnode):
    class Meta:
        name = "X3DFontStyleNode"


@dataclass
class X3DgeometricPropertyNode(X3Dnode):
    class Meta:
        name = "X3DGeometricPropertyNode"


@dataclass
class X3DgeometryNode(X3Dnode):
    class Meta:
        name = "X3DGeometryNode"


@dataclass
class X3DlayerNode(X3Dnode):
    class Meta:
        name = "X3DLayerNode"

    is_pickable: bool = field(
        default=True,
        metadata={
            "name": "isPickable",
            "type": "Attribute",
        }
    )


@dataclass
class X3DnbodyCollisionSpaceNode(X3Dnode):
    class Meta:
        name = "X3DNBodyCollisionSpaceNode"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DnurbsControlCurveNode(X3Dnode):
    class Meta:
        name = "X3DNurbsControlCurveNode"

    control_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )


@dataclass
class X3DparticleEmitterNode(X3Dnode):
    class Meta:
        name = "X3DParticleEmitterNode"

    speed: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    variation: float = field(
        default=0.25,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    mass: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    surface_area: float = field(
        default=0.0,
        metadata={
            "name": "surfaceArea",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )


@dataclass
class X3DparticlePhysicsModelNode(X3Dnode):
    class Meta:
        name = "X3DParticlePhysicsModelNode"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DrigidJointNode(X3Dnode):
    """
    :ivar rigid_body: body1, body2
    :ivar proto_instance: Appropriately typed substitution node
    :ivar force_output:
    """
    class Meta:
        name = "X3DRigidJointNode"

    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    force_output: List[str] = field(
        default_factory=lambda: [
            "\"NONE\"",
        ],
        metadata={
            "name": "forceOutput",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class X3DvolumeRenderStyleNode(X3Dnode):
    class Meta:
        name = "X3DVolumeRenderStyleNode"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Appearance(X3DappearanceNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="appearance",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Arc2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    radius: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    start_angle: float = field(
        default=0.0,
        metadata={
            "name": "startAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    end_angle: float = field(
        default=1.570796,
        metadata={
            "name": "endAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ArcClose2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    radius: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    start_angle: float = field(
        default=0.0,
        metadata={
            "name": "startAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    end_angle: float = field(
        default=1.570796,
        metadata={
            "name": "endAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    closure_type: ClosureTypeChoices = field(
        default=ClosureTypeChoices.PIE,
        metadata={
            "name": "closureType",
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BallJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor_point: str = field(
        default="0 0 0",
        metadata={
            "name": "anchorPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BooleanFilter(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BooleanToggle(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    toggle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BoundedPhysicsModel(X3DparticlePhysicsModelNode):
    """
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    box: Optional["Box"] = field(
        default=None,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: Optional["Cone"] = field(
        default=None,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: Optional["Cylinder"] = field(
        default=None,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: Optional["IndexedFaceSet"] = field(
        default=None,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: Optional["IndexedLineSet"] = field(
        default=None,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: Optional["IndexedTriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: Optional["IndexedTriangleSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: Optional["IndexedTriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: Optional["LineSet"] = field(
        default=None,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: Optional["PointSet"] = field(
        default=None,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: Optional["Sphere"] = field(
        default=None,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: Optional["TriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: Optional["TriangleSet"] = field(
        default=None,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: Optional["TriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: Optional["ElevationGrid"] = field(
        default=None,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: Optional["Polyline2D"] = field(
        default=None,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: Optional["Polypoint2D"] = field(
        default=None,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: Optional["Rectangle2D"] = field(
        default=None,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: Optional["TriangleSet2D"] = field(
        default=None,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: Optional["Extrusion"] = field(
        default=None,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: Optional["Text"] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: Optional["Arc2D"] = field(
        default=None,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: Optional["ArcClose2D"] = field(
        default=None,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: Optional["Circle2D"] = field(
        default=None,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: Optional["Disk2D"] = field(
        default=None,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: Optional["QuadSet"] = field(
        default=None,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: Optional["IndexedQuadSet"] = field(
        default=None,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: Optional["GeoElevationGrid"] = field(
        default=None,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: Optional["NurbsCurve"] = field(
        default=None,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: Optional["NurbsPatchSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: Optional["NurbsSweptSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: Optional["NurbsSwungSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: Optional["NurbsTrimmedSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="physics",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Box(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    size: str = field(
        default="2 2 2",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Circle2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    radius: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ClipPlane(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    plane: str = field(
        default="0 1 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CollisionCollection(X3DchildNode):
    """
    :ivar collidable_offset:
    :ivar collidable_shape:
    :ivar collision_space:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar applied_parameters: Array of appliedParametersChoices. Note
        that strict validation of appliedParameters enumeration values
        does not occur via schema since MFString allows any value in any
        order.
    :ivar bounce:
    :ivar enabled:
    :ivar friction_coefficients:
    :ivar min_bounce_speed:
    :ivar slip_factors:
    :ivar softness_constant_force_mix:
    :ivar softness_error_correction:
    :ivar surface_speed:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_space: List["CollisionSpace"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSpace",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    applied_parameters: List[str] = field(
        default_factory=lambda: [
            "\"BOUNCE\"",
        ],
        metadata={
            "name": "appliedParameters",
            "type": "Attribute",
            "tokens": True,
        }
    )
    bounce: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    friction_coefficients: str = field(
        default="0 0",
        metadata={
            "name": "frictionCoefficients",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    min_bounce_speed: float = field(
        default=0.1,
        metadata={
            "name": "minBounceSpeed",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    slip_factors: str = field(
        default="0 0",
        metadata={
            "name": "slipFactors",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    softness_constant_force_mix: float = field(
        default=0.0001,
        metadata={
            "name": "softnessConstantForceMix",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    softness_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "softnessErrorCorrection",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    surface_speed: str = field(
        default="0 0",
        metadata={
            "name": "surfaceSpeed",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="collider",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CollisionSpace(X3DnbodyCollisionSpaceNode):
    """
    :ivar collidable_offset: collider
    :ivar collidable_shape: collider
    :ivar collision_space: collider
    :ivar proto_instance: Appropriately typed substitution node
    :ivar use_geometry:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    collidable_offset: List["CollidableOffset"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_space: List["CollisionSpace"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSpace",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    use_geometry: bool = field(
        default=False,
        metadata={
            "name": "useGeometry",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cone(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    bottom: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    bottom_radius: float = field(
        default=1.0,
        metadata={
            "name": "bottomRadius",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    height: float = field(
        default=2.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    side: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ConeEmitter(X3DparticleEmitterNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    angle: float = field(
        default=0.7854,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 3.1416,
        }
    )
    direction: str = field(
        default="0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    position: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ContourPolyline2D(X3DnurbsControlCurveNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cylinder(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    bottom: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    height: float = field(
        default=2.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    radius: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    side: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    top: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class DisentityManager(X3DchildNode):
    """
    :ivar disentity_type_mapping:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar address:
    :ivar application_id:
    :ivar port:
    :ivar site_id:
    :ivar container_field:
    """
    class Meta:
        name = "DISEntityManager"
        namespace = "http://www.design2machine.com"

    disentity_type_mapping: List["DisentityTypeMapping"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityTypeMapping",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    address: str = field(
        default="localhost",
        metadata={
            "type": "Attribute",
        }
    )
    application_id: int = field(
        default=0,
        metadata={
            "name": "applicationID",
            "type": "Attribute",
        }
    )
    port: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    site_id: int = field(
        default=0,
        metadata={
            "name": "siteID",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Disk2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    inner_radius: float = field(
        default=0.0,
        metadata={
            "name": "innerRadius",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    outer_radius: float = field(
        default=1.0,
        metadata={
            "name": "outerRadius",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class DoubleAxisHingeJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor_point: str = field(
        default="0 0 0",
        metadata={
            "name": "anchorPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    axis1: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    axis2: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    desired_angular_velocity1: float = field(
        default=0.0,
        metadata={
            "name": "desiredAngularVelocity1",
            "type": "Attribute",
        }
    )
    desired_angular_velocity2: float = field(
        default=0.0,
        metadata={
            "name": "desiredAngularVelocity2",
            "type": "Attribute",
        }
    )
    max_angle1: float = field(
        default=3.141592653,
        metadata={
            "name": "maxAngle1",
            "type": "Attribute",
        }
    )
    max_torque1: float = field(
        default=0.0,
        metadata={
            "name": "maxTorque1",
            "type": "Attribute",
        }
    )
    max_torque2: float = field(
        default=0.0,
        metadata={
            "name": "maxTorque2",
            "type": "Attribute",
        }
    )
    min_angle1: float = field(
        default=-3.141592653,
        metadata={
            "name": "minAngle1",
            "type": "Attribute",
        }
    )
    stop1_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop1Bounce",
            "type": "Attribute",
        }
    )
    stop1_constant_force_mix: float = field(
        default=0.001,
        metadata={
            "name": "stop1ConstantForceMix",
            "type": "Attribute",
        }
    )
    stop1_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop1ErrorCorrection",
            "type": "Attribute",
        }
    )
    suspension_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "suspensionErrorCorrection",
            "type": "Attribute",
        }
    )
    suspension_force: float = field(
        default=0.0,
        metadata={
            "name": "suspensionForce",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class EaseInEaseOut(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    ease_in_ease_out: Optional[str] = field(
        default=None,
        metadata={
            "name": "easeInEaseOut",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ElevationGrid(X3DgeometryNode):
    """
    :ivar float_vertex_attribute: attrib
    :ivar matrix3_vertex_attribute: attrib
    :ivar matrix4_vertex_attribute: attrib
    :ivar color: color
    :ivar color_rgba: color
    :ivar fog_coordinate: fogcoord
    :ivar normal: normal
    :ivar texture_coordinate: texcoord
    :ivar texture_coordinate3_d: texcoord
    :ivar texture_coordinate4_d: texcoord
    :ivar texture_coordinate_generator: texcoord
    :ivar multi_texture_coordinate: texcoord
    :ivar proto_instance: Appropriately typed substitution node
    :ivar height:
    :ivar ccw:
    :ivar color_per_vertex:
    :ivar crease_angle:
    :ivar normal_per_vertex:
    :ivar solid:
    :ivar x_dimension:
    :ivar x_spacing:
    :ivar z_dimension:
    :ivar z_spacing:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    float_vertex_attribute: Optional["FloatVertexAttribute"] = field(
        default=None,
        metadata={
            "name": "FloatVertexAttribute",
            "type": "Element",
        }
    )
    matrix3_vertex_attribute: Optional["Matrix3VertexAttribute"] = field(
        default=None,
        metadata={
            "name": "Matrix3VertexAttribute",
            "type": "Element",
        }
    )
    matrix4_vertex_attribute: Optional["Matrix4VertexAttribute"] = field(
        default=None,
        metadata={
            "name": "Matrix4VertexAttribute",
            "type": "Element",
        }
    )
    color: Optional["Color"] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        }
    )
    color_rgba: Optional["ColorRgba"] = field(
        default=None,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
        }
    )
    fog_coordinate: Optional["FogCoordinate"] = field(
        default=None,
        metadata={
            "name": "FogCoordinate",
            "type": "Element",
        }
    )
    normal: Optional["Normal"] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
        }
    )
    texture_coordinate: Optional["TextureCoordinate"] = field(
        default=None,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    texture_coordinate3_d: Optional["TextureCoordinate3D"] = field(
        default=None,
        metadata={
            "name": "TextureCoordinate3D",
            "type": "Element",
        }
    )
    texture_coordinate4_d: Optional["TextureCoordinate4D"] = field(
        default=None,
        metadata={
            "name": "TextureCoordinate4D",
            "type": "Element",
        }
    )
    texture_coordinate_generator: Optional["TextureCoordinateGenerator"] = field(
        default=None,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
        }
    )
    multi_texture_coordinate: Optional["MultiTextureCoordinate"] = field(
        default=None,
        metadata={
            "name": "MultiTextureCoordinate",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    height: str = field(
        default="0 0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    color_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "colorPerVertex",
            "type": "Attribute",
        }
    )
    crease_angle: float = field(
        default=0.0,
        metadata={
            "name": "creaseAngle",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    normal_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "normalPerVertex",
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    x_dimension: int = field(
        default=2,
        metadata={
            "name": "xDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    x_spacing: float = field(
        default=1.0,
        metadata={
            "name": "xSpacing",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    z_dimension: int = field(
        default=2,
        metadata={
            "name": "zDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    z_spacing: float = field(
        default=1.0,
        metadata={
            "name": "zSpacing",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ExplosionEmitter(X3DparticleEmitterNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    position: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Extrusion(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    begin_cap: bool = field(
        default=True,
        metadata={
            "name": "beginCap",
            "type": "Attribute",
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    convex: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    crease_angle: float = field(
        default=0.0,
        metadata={
            "name": "creaseAngle",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    cross_section: str = field(
        default="1 1 1 -1 -1 -1 -1 1 1 1",
        metadata={
            "name": "crossSection",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    end_cap: bool = field(
        default=True,
        metadata={
            "name": "endCap",
            "type": "Attribute",
        }
    )
    orientation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    scale: str = field(
        default="1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    spine: str = field(
        default="0 0 0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class FillProperties(X3DappearanceChildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    filled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    hatched: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    hatch_style: int = field(
        default=1,
        metadata={
            "name": "hatchStyle",
            "type": "Attribute",
        }
    )
    hatch_color: str = field(
        default="1 1 1",
        metadata={
            "name": "hatchColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    container_field: str = field(
        default="fillProperties",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class FogCoordinate(X3DgeometricPropertyNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    depth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="fogCoord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class FontStyle(X3DfontStyleNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    family: List[str] = field(
        default_factory=lambda: [
            "\"SERIF\"",
        ],
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    horizontal: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    justify: JustifyChoices = field(
        default=JustifyChoices.BEGIN,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    left_to_right: bool = field(
        default=True,
        metadata={
            "name": "leftToRight",
            "type": "Attribute",
        }
    )
    size: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    spacing: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    style: FontStyleChoices = field(
        default=FontStyleChoices.PLAIN,
        metadata={
            "type": "Attribute",
        }
    )
    top_to_bottom: bool = field(
        default=True,
        metadata={
            "name": "topToBottom",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="fontStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ForcePhysicsModel(X3DparticlePhysicsModelNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    force: str = field(
        default="0 -9.8 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="physics",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoElevationGrid(X3DgeometryNode):
    """
    :ivar geo_origin:
    :ivar color:
    :ivar color_rgba:
    :ivar normal:
    :ivar texture_coordinate:
    :ivar texture_coordinate_generator:
    :ivar multi_texture_coordinate:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar fog_coordinate:
    :ivar geo_system:
    :ivar geo_grid_origin:
    :ivar height:
    :ivar ccw:
    :ivar color_per_vertex:
    :ivar crease_angle:
    :ivar normal_per_vertex:
    :ivar solid:
    :ivar x_dimension:
    :ivar x_spacing:
    :ivar y_scale:
    :ivar z_dimension:
    :ivar z_spacing:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: List["GeoOrigin"] = field(
        default_factory=list,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    texture_coordinate_generator: List["TextureCoordinateGenerator"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    multi_texture_coordinate: List["MultiTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureCoordinate",
            "type": "Element",
            "max_occurs": 20,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 34,
            "sequential": True,
        }
    )
    fog_coordinate: List["FogCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "FogCoordinate",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_grid_origin: str = field(
        default="0 0 0",
        metadata={
            "name": "geoGridOrigin",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    height: str = field(
        default="0 0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    color_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "colorPerVertex",
            "type": "Attribute",
        }
    )
    crease_angle: float = field(
        default=0.0,
        metadata={
            "name": "creaseAngle",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    normal_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "normalPerVertex",
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    x_dimension: int = field(
        default=2,
        metadata={
            "name": "xDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    x_spacing: float = field(
        default=1.0,
        metadata={
            "name": "xSpacing",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    y_scale: float = field(
        default=1.0,
        metadata={
            "name": "yScale",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    z_dimension: int = field(
        default=2,
        metadata={
            "name": "zDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    z_spacing: float = field(
        default=1.0,
        metadata={
            "name": "zSpacing",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoLod(X3DchildNode):
    """
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar route:
    :ivar extern_proto_declare:
    :ivar proto_declare:
    :ivar import_value:
    :ivar export:
    :ivar geo_origin: geoOrigin SFNode
    :ivar geo_system:
    :ivar root_url:
    :ivar child1_url:
    :ivar child2_url:
    :ivar child3_url:
    :ivar child4_url:
    :ivar center:
    :ivar range:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        name = "GeoLOD"
        namespace = "http://www.design2machine.com"

    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "ROUTE",
            "type": "Element",
        }
    )
    extern_proto_declare: List[ExternProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ExternProtoDeclare",
            "type": "Element",
        }
    )
    proto_declare: List["ProtoDeclare"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoDeclare",
            "type": "Element",
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "IMPORT",
            "type": "Element",
        }
    )
    export: List[Export] = field(
        default_factory=list,
        metadata={
            "name": "EXPORT",
            "type": "Element",
        }
    )
    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    root_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "rootUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    child1_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "child1Url",
            "type": "Attribute",
            "tokens": True,
        }
    )
    child2_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "child2Url",
            "type": "Attribute",
            "tokens": True,
        }
    )
    child3_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "child3Url",
            "type": "Attribute",
            "tokens": True,
        }
    )
    child4_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "child4Url",
            "type": "Attribute",
            "tokens": True,
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    range: float = field(
        default=10.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class HanimDisplacer(X3DgeometricPropertyNode):
    class Meta:
        name = "HAnimDisplacer"
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    displacements: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    weight: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="displacers",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class HanimHumanoid(X3DchildNode):
    """
    :ivar hanim_joint: SFNode skeleton, or MFNode joints (USE nodes)
    :ivar hanim_segment: MFNode segments (USE nodes)
    :ivar hanim_site: SFNode skeleton, or MFNode sites/viewpoints (USE
        nodes)
    :ivar group:
    :ivar transform:
    :ivar shape:
    :ivar indexed_face_set:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar normal: SFNode skinNormal
    :ivar proto_instance: Appropriately typed substitution node
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar center:
    :ivar info:
    :ivar name:
    :ivar rotation:
    :ivar scale:
    :ivar scale_orientation:
    :ivar translation:
    :ivar version:
    :ivar container_field:
    """
    class Meta:
        name = "HAnimHumanoid"
        namespace = "http://www.design2machine.com"

    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    indexed_face_set: List["IndexedFaceSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "sequential": True,
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    info: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    version: HanimVersionChoices = field(
        default=HanimVersionChoices.VALUE_1_0,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class HanimJoint(X3DchildNode):
    """
    :ivar hanim_joint: children
    :ivar hanim_segment: children
    :ivar hanim_site: children
    :ivar hanim_displacer: displacers
    :ivar proto_instance: Appropriately typed substitution node
    :ivar name:
    :ivar center:
    :ivar rotation:
    :ivar scale:
    :ivar scale_orientation:
    :ivar translation:
    :ivar skin_coord_index:
    :ivar skin_coord_weight:
    :ivar llimit:
    :ivar ulimit:
    :ivar limit_orientation:
    :ivar stiffness:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        name = "HAnimJoint"
        namespace = "http://www.design2machine.com"

    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    hanim_displacer: List["HanimDisplacer"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimDisplacer",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    skin_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "skinCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    skin_coord_weight: Optional[str] = field(
        default=None,
        metadata={
            "name": "skinCoordWeight",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    llimit: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    ulimit: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    limit_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "limitOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    stiffness: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: ContainerFieldChoicesHanimJoint = field(
        default=ContainerFieldChoicesHanimJoint.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedLineSet(X3DgeometryNode):
    """
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar geo_coordinate:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar color_per_vertex:
    :ivar color_index:
    :ivar coord_index:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    color_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "colorPerVertex",
            "type": "Attribute",
        }
    )
    color_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "colorIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Inline(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    load: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3DurlObject = field(
        default=ContainerFieldChoicesX3DurlObject.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Layer(X3DlayerNode):
    """
    :ivar viewport: viewport
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
            "sequential": True,
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
            "sequential": True,
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
            "sequential": True,
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
            "sequential": True,
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
            "sequential": True,
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
            "sequential": True,
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
            "sequential": True,
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
            "sequential": True,
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
            "sequential": True,
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
            "sequential": True,
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
            "sequential": True,
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
            "sequential": True,
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
            "sequential": True,
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
            "sequential": True,
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
            "sequential": True,
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
            "sequential": True,
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
            "sequential": True,
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: str = field(
        default="layers",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LayoutLayer(X3DlayerNode):
    """
    :ivar layout: layout
    :ivar viewport: viewport
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    layout: List["Layout"] = field(
        default_factory=list,
        metadata={
            "name": "Layout",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="layers",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LineProperties(X3DappearanceChildNode):
    """
    :ivar applied:
    :ivar linetype: TODO inconsistent camel-case spelling, should be
        lineType: Mantis 1252
    :ivar linewidth_scale_factor: TODO inconsistent camel-case spelling,
        should be lineWidthScaleFactor: Mantis 1252
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    applied: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    linetype: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    linewidth_scale_factor: float = field(
        default=0.0,
        metadata={
            "name": "linewidthScaleFactor",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="lineProperties",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LineSet(X3DgeometryNode):
    """
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar geo_coordinate:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar vertex_count:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    vertex_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertexCount",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LocalFog(X3DchildNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    color: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    fog_type: FogTypeChoices = field(
        default=FogTypeChoices.LINEAR,
        metadata={
            "name": "fogType",
            "type": "Attribute",
        }
    )
    visibility_range: float = field(
        default=0.0,
        metadata={
            "name": "visibilityRange",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MotorJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    auto_calc: bool = field(
        default=False,
        metadata={
            "name": "autoCalc",
            "type": "Attribute",
        }
    )
    axis1_angle: float = field(
        default=0.0,
        metadata={
            "name": "axis1Angle",
            "type": "Attribute",
        }
    )
    axis1_torque: float = field(
        default=0.0,
        metadata={
            "name": "axis1Torque",
            "type": "Attribute",
        }
    )
    axis2_angle: float = field(
        default=0.0,
        metadata={
            "name": "axis2Angle",
            "type": "Attribute",
        }
    )
    axis2_torque: float = field(
        default=0.0,
        metadata={
            "name": "axis2Torque",
            "type": "Attribute",
        }
    )
    axis3_angle: float = field(
        default=0.0,
        metadata={
            "name": "axis3Angle",
            "type": "Attribute",
        }
    )
    axis3_torque: float = field(
        default=0.0,
        metadata={
            "name": "axis3Torque",
            "type": "Attribute",
        }
    )
    enabled_axes: int = field(
        default=1,
        metadata={
            "name": "enabledAxes",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 3,
        }
    )
    motor1_axis: str = field(
        default="0 0 0",
        metadata={
            "name": "motor1Axis",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    motor2_axis: str = field(
        default="0 0 0",
        metadata={
            "name": "motor2Axis",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    motor3_axis: str = field(
        default="0 0 0",
        metadata={
            "name": "motor3Axis",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    stop1_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop1Bounce",
            "type": "Attribute",
        }
    )
    stop1_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop1ErrorCorrection",
            "type": "Attribute",
        }
    )
    stop2_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop2Bounce",
            "type": "Attribute",
        }
    )
    stop2_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop2ErrorCorrection",
            "type": "Attribute",
        }
    )
    stop3_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop3Bounce",
            "type": "Attribute",
        }
    )
    stop3_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop3ErrorCorrection",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsCurve2D(X3DnurbsControlCurveNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    closed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    knot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    order: int = field(
        default=3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    tessellation: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsOrientationInterpolator(X3DchildNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar knot:
    :ivar order:
    :ivar weight:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    knot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    order: int = field(
        default=3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsPositionInterpolator(X3DchildNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar knot:
    :ivar order:
    :ivar weight:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    knot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    order: int = field(
        default=3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsSet(X3DchildNode):
    """
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar tessellation_scale:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    tessellation_scale: float = field(
        default=1.0,
        metadata={
            "name": "tessellationScale",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsSurfaceInterpolator(X3DchildNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar u_dimension:
    :ivar v_dimension:
    :ivar u_knot:
    :ivar v_knot:
    :ivar u_order:
    :ivar v_order:
    :ivar weight:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    u_dimension: int = field(
        default=0,
        metadata={
            "name": "uDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    v_dimension: int = field(
        default=0,
        metadata={
            "name": "vDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    u_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "uKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    v_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "vKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    u_order: int = field(
        default=3,
        metadata={
            "name": "uOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    v_order: int = field(
        default=3,
        metadata={
            "name": "vOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PointEmitter(X3DparticleEmitterNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    direction: str = field(
        default="0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    position: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PointSet(X3DgeometryNode):
    """
    :ivar color:
    :ivar color_rgba:
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar geo_coordinate:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Polyline2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    line_segments: Optional[str] = field(
        default=None,
        metadata={
            "name": "lineSegments",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PolylineEmitter(X3DparticleEmitterNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar coord_index:
    :ivar direction:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    coord_index: str = field(
        default="-1",
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    direction: str = field(
        default="0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Polypoint2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ProjectionVolumeStyle(X3DvolumeRenderStyleNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    intensity_threshold: float = field(
        default=0.0,
        metadata={
            "name": "intensityThreshold",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    type: str = field(
        default="MAX",
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Rectangle2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    size: str = field(
        default="2 2",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class RigidBodyCollection(X3DchildNode):
    """
    :ivar collision_collection: collider
    :ivar rigid_body: bodies
    :ivar ball_joint: massDensityModel
    :ivar double_axis_hinge_joint: massDensityModel
    :ivar motor_joint: massDensityModel
    :ivar single_axis_hinge_joint: massDensityModel
    :ivar slider_joint: massDensityModel
    :ivar universal_joint: massDensityModel
    :ivar proto_instance: Appropriately typed substitution node
    :ivar auto_disable:
    :ivar constant_force_mix:
    :ivar contact_surface_thickness:
    :ivar disable_angular_speed:
    :ivar disable_linear_speed:
    :ivar disable_time:
    :ivar enabled:
    :ivar error_correction:
    :ivar gravity:
    :ivar iterations:
    :ivar max_correction_speed:
    :ivar prefer_accuracy:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    collision_collection: List["CollisionCollection"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionCollection",
            "type": "Element",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    rigid_body: List["RigidBody"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBody",
            "type": "Element",
            "sequential": True,
        }
    )
    ball_joint: List["BallJoint"] = field(
        default_factory=list,
        metadata={
            "name": "BallJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    double_axis_hinge_joint: List["DoubleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "DoubleAxisHingeJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    motor_joint: List["MotorJoint"] = field(
        default_factory=list,
        metadata={
            "name": "MotorJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    single_axis_hinge_joint: List["SingleAxisHingeJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SingleAxisHingeJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    slider_joint: List["SliderJoint"] = field(
        default_factory=list,
        metadata={
            "name": "SliderJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    universal_joint: List["UniversalJoint"] = field(
        default_factory=list,
        metadata={
            "name": "UniversalJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    auto_disable: bool = field(
        default=False,
        metadata={
            "name": "autoDisable",
            "type": "Attribute",
        }
    )
    constant_force_mix: float = field(
        default=0.0001,
        metadata={
            "name": "constantForceMix",
            "type": "Attribute",
        }
    )
    contact_surface_thickness: float = field(
        default=0.0,
        metadata={
            "name": "contactSurfaceThickness",
            "type": "Attribute",
        }
    )
    disable_angular_speed: float = field(
        default=0.0,
        metadata={
            "name": "disableAngularSpeed",
            "type": "Attribute",
        }
    )
    disable_linear_speed: float = field(
        default=0.0,
        metadata={
            "name": "disableLinearSpeed",
            "type": "Attribute",
        }
    )
    disable_time: float = field(
        default=0.0,
        metadata={
            "name": "disableTime",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    error_correction: float = field(
        default=0.8,
        metadata={
            "name": "errorCorrection",
            "type": "Attribute",
        }
    )
    gravity: str = field(
        default="0 -9.8 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    iterations: int = field(
        default=10,
        metadata={
            "type": "Attribute",
        }
    )
    max_correction_speed: float = field(
        default=-1.0,
        metadata={
            "name": "maxCorrectionSpeed",
            "type": "Attribute",
        }
    )
    prefer_accuracy: bool = field(
        default=False,
        metadata={
            "name": "preferAccuracy",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ScreenFontStyle(X3DfontStyleNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    family: List[str] = field(
        default_factory=lambda: [
            "\"SERIF\"",
        ],
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    horizontal: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    justify: JustifyChoices = field(
        default=JustifyChoices.BEGIN,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    left_to_right: bool = field(
        default=True,
        metadata={
            "name": "leftToRight",
            "type": "Attribute",
        }
    )
    point_size: float = field(
        default=12.0,
        metadata={
            "name": "pointSize",
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    spacing: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    style: FontStyleChoices = field(
        default=FontStyleChoices.PLAIN,
        metadata={
            "type": "Attribute",
        }
    )
    top_to_bottom: bool = field(
        default=True,
        metadata={
            "name": "topToBottom",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="fontStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SingleAxisHingeJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor_point: str = field(
        default="0 0 0",
        metadata={
            "name": "anchorPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    axis: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    max_angle: float = field(
        default=3.141592653,
        metadata={
            "name": "maxAngle",
            "type": "Attribute",
        }
    )
    min_angle: float = field(
        default=-3.141592653,
        metadata={
            "name": "minAngle",
            "type": "Attribute",
        }
    )
    stop_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stopBounce",
            "type": "Attribute",
        }
    )
    stop_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stopErrorCorrection",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SliderJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    axis: str = field(
        default="0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    max_separation: float = field(
        default=1.0,
        metadata={
            "name": "maxSeparation",
            "type": "Attribute",
        }
    )
    min_separation: float = field(
        default=0.0,
        metadata={
            "name": "minSeparation",
            "type": "Attribute",
        }
    )
    slider_force: float = field(
        default=0.0,
        metadata={
            "name": "sliderForce",
            "type": "Attribute",
        }
    )
    stop_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stopBounce",
            "type": "Attribute",
        }
    )
    stop_error_correction: float = field(
        default=1.0,
        metadata={
            "name": "stopErrorCorrection",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Sphere(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    radius: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class StaticGroup(X3DchildNode):
    """
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar route:
    :ivar extern_proto_declare:
    :ivar proto_declare:
    :ivar import_value:
    :ivar export:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
            "sequential": True,
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
            "sequential": True,
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
            "sequential": True,
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
            "sequential": True,
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
            "sequential": True,
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
            "sequential": True,
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
            "sequential": True,
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
            "sequential": True,
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
            "sequential": True,
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
            "sequential": True,
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
            "sequential": True,
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
            "sequential": True,
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
            "sequential": True,
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
            "sequential": True,
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
            "sequential": True,
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
            "sequential": True,
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
            "sequential": True,
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
            "sequential": True,
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
            "sequential": True,
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
            "sequential": True,
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
            "sequential": True,
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "ROUTE",
            "type": "Element",
            "sequential": True,
        }
    )
    extern_proto_declare: List[ExternProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ExternProtoDeclare",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_declare: List["ProtoDeclare"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoDeclare",
            "type": "Element",
            "sequential": True,
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "IMPORT",
            "type": "Element",
            "sequential": True,
        }
    )
    export: List[Export] = field(
        default_factory=list,
        metadata={
            "name": "EXPORT",
            "type": "Element",
            "sequential": True,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SurfaceEmitter(X3DparticleEmitterNode):
    """
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar coord_index:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    box: Optional["Box"] = field(
        default=None,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: Optional["Cone"] = field(
        default=None,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: Optional["Cylinder"] = field(
        default=None,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: Optional["IndexedFaceSet"] = field(
        default=None,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: Optional["IndexedLineSet"] = field(
        default=None,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: Optional["IndexedTriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: Optional["IndexedTriangleSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: Optional["IndexedTriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: Optional["LineSet"] = field(
        default=None,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: Optional["PointSet"] = field(
        default=None,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: Optional["Sphere"] = field(
        default=None,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: Optional["TriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: Optional["TriangleSet"] = field(
        default=None,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: Optional["TriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: Optional["ElevationGrid"] = field(
        default=None,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: Optional["Polyline2D"] = field(
        default=None,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: Optional["Polypoint2D"] = field(
        default=None,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: Optional["Rectangle2D"] = field(
        default=None,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: Optional["TriangleSet2D"] = field(
        default=None,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: Optional["Extrusion"] = field(
        default=None,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: Optional["Text"] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: Optional["Arc2D"] = field(
        default=None,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: Optional["ArcClose2D"] = field(
        default=None,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: Optional["Circle2D"] = field(
        default=None,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: Optional["Disk2D"] = field(
        default=None,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: Optional["QuadSet"] = field(
        default=None,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: Optional["IndexedQuadSet"] = field(
        default=None,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: Optional["GeoElevationGrid"] = field(
        default=None,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: Optional["NurbsCurve"] = field(
        default=None,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: Optional["NurbsPatchSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: Optional["NurbsSweptSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: Optional["NurbsSwungSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: Optional["NurbsTrimmedSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    coord_index: str = field(
        default="-1",
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Text(X3DgeometryNode):
    """
    :ivar font_style:
    :ivar screen_font_style:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar string:
    :ivar length:
    :ivar max_extent:
    :ivar solid:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    font_style: Optional["FontStyle"] = field(
        default=None,
        metadata={
            "name": "FontStyle",
            "type": "Element",
        }
    )
    screen_font_style: Optional["ScreenFontStyle"] = field(
        default=None,
        metadata={
            "name": "ScreenFontStyle",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    string: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    length: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    max_extent: float = field(
        default=0.0,
        metadata={
            "name": "maxExtent",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TriangleSet2D(X3DgeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    vertices: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalJoint(X3DrigidJointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor_point: str = field(
        default="0 0 0",
        metadata={
            "name": "anchorPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    axis1: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    axis2: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    stop1_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop1Bounce",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    stop1_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop1ErrorCorrection",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    stop2_bounce: float = field(
        default=0.0,
        metadata={
            "name": "stop2Bounce",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    stop2_error_correction: float = field(
        default=0.8,
        metadata={
            "name": "stop2ErrorCorrection",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    container_field: str = field(
        default="joints",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ViewpointGroup(X3DchildNode):
    """
    :ivar viewpoint:
    :ivar ortho_viewpoint:
    :ivar geo_viewpoint:
    :ivar viewpoint_group:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar center:
    :ivar description:
    :ivar displayed:
    :ivar retain_user_offsets:
    :ivar size:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    displayed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    retain_user_offsets: bool = field(
        default=False,
        metadata={
            "name": "retainUserOffsets",
            "type": "Attribute",
        }
    )
    size: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class VolumeEmitter(X3DparticleEmitterNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar coord_index:
    :ivar direction:
    :ivar internal:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    coord_index: str = field(
        default="-1",
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    direction: str = field(
        default="0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    internal: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="emitter",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class WindPhysicsModel(X3DparticlePhysicsModelNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    direction: str = field(
        default="1 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    gustiness: float = field(
        default=0.1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    speed: float = field(
        default=0.1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    turbulence: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    container_field: str = field(
        default="physics",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3DbindableNode(X3DchildNode):
    class Meta:
        name = "X3DBindableNode"


@dataclass
class X3DcolorNode(X3DgeometricPropertyNode):
    class Meta:
        name = "X3DColorNode"


@dataclass
class X3DcomposableVolumeRenderStyleNode(X3DvolumeRenderStyleNode):
    class Meta:
        name = "X3DComposableVolumeRenderStyleNode"


@dataclass
class X3DcomposedGeometryNode(X3DgeometryNode):
    """
    :ivar float_vertex_attribute: attrib
    :ivar matrix3_vertex_attribute: attrib
    :ivar matrix4_vertex_attribute: attrib
    :ivar color: color
    :ivar color_rgba: color
    :ivar coordinate: coord
    :ivar coordinate_double: coord
    :ivar geo_coordinate: coord
    :ivar fog_coordinate: fogcoord
    :ivar normal: normal
    :ivar texture_coordinate: texcoord
    :ivar texture_coordinate3_d: texcoord
    :ivar texture_coordinate4_d: texcoord
    :ivar texture_coordinate_generator: texcoord
    :ivar multi_texture_coordinate: texcoord
    :ivar nurbs_texture_coordinate: texcoord
    :ivar proto_instance: Appropriately typed substitution node
    :ivar ccw:
    :ivar color_per_vertex:
    :ivar normal_per_vertex:
    :ivar solid:
    """
    class Meta:
        name = "X3DComposedGeometryNode"

    float_vertex_attribute: List["FloatVertexAttribute"] = field(
        default_factory=list,
        metadata={
            "name": "FloatVertexAttribute",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    matrix3_vertex_attribute: List["Matrix3VertexAttribute"] = field(
        default_factory=list,
        metadata={
            "name": "Matrix3VertexAttribute",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    matrix4_vertex_attribute: List["Matrix4VertexAttribute"] = field(
        default_factory=list,
        metadata={
            "name": "Matrix4VertexAttribute",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    color: List["Color"] = field(
        default_factory=list,
        metadata={
            "name": "Color",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    color_rgba: List["ColorRgba"] = field(
        default_factory=list,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    fog_coordinate: List["FogCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "FogCoordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    normal: List["Normal"] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_coordinate3_d: List["TextureCoordinate3D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate3D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_coordinate4_d: List["TextureCoordinate4D"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate4D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    texture_coordinate_generator: List["TextureCoordinateGenerator"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    multi_texture_coordinate: List["MultiTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTextureCoordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    color_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "colorPerVertex",
            "type": "Attribute",
        }
    )
    normal_per_vertex: bool = field(
        default=True,
        metadata={
            "name": "normalPerVertex",
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DcoordinateNode(X3DgeometricPropertyNode):
    class Meta:
        name = "X3DCoordinateNode"


@dataclass
class X3DfollowerNode(X3DchildNode):
    class Meta:
        name = "X3DFollowerNode"


@dataclass
class X3DgroupingNode(X3DchildNode):
    """
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar route:
    :ivar extern_proto_declare:
    :ivar proto_declare:
    :ivar import_value:
    :ivar export:
    :ivar bbox_center:
    :ivar bbox_size:
    """
    class Meta:
        name = "X3DGroupingNode"

    background: List["Background"] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    color_interpolator: List["ColorInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    coordinate_interpolator: List["CoordinateInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    directional_light: List["DirectionalLight"] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    navigation_info: List["NavigationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    normal_interpolator: List["NormalInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    orientation_interpolator: List["OrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_interpolator: List["PositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    scalar_interpolator: List["ScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    time_sensor: List["TimeSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    viewpoint: List["Viewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    world_info: List["WorldInfo"] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    boolean_filter: List["BooleanFilter"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    boolean_sequencer: List["BooleanSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    boolean_toggle: List["BooleanToggle"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    boolean_trigger: List["BooleanTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    cylinder_sensor: List["CylinderSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    integer_sequencer: List["IntegerSequencer"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    integer_trigger: List["IntegerTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    key_sensor: List["KeySensor"] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    plane_sensor: List["PlaneSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    point_light: List["PointLight"] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    proximity_sensor: List["ProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    sphere_sensor: List["SphereSensor"] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    spot_light: List["SpotLight"] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    string_sensor: List["StringSensor"] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    time_trigger: List["TimeTrigger"] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    touch_sensor: List["TouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    fog: List["Fog"] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    load_sensor: List["LoadSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    local_fog: List["LocalFog"] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    sound: List["Sound"] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    visibility_sensor: List["VisibilitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    coordinate_interpolator2_d: List["CoordinateInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_interpolator2_d: List["PositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    clip_plane: List["ClipPlane"] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    ease_in_ease_out: List["EaseInEaseOut"] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    line_pick_sensor: List["LinePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    pickable_group: List["PickableGroup"] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    point_pick_sensor: List["PointPickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    primitive_pick_sensor: List["PrimitivePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    volume_pick_sensor: List["VolumePickSensor"] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    spline_position_interpolator: List["SplinePositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    spline_position_interpolator2_d: List["SplinePositionInterpolator2D"] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    spline_scalar_interpolator: List["SplineScalarInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    squad_orientation_interpolator: List["SquadOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    ortho_viewpoint: List["OrthoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    viewpoint_group: List["ViewpointGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    color_chaser: List["ColorChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    color_damper: List["ColorDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    coordinate_chaser: List["CoordinateChaser"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    coordinate_damper: List["CoordinateDamper"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    orientation_chaser: List["OrientationChaser"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    orientation_damper: List["OrientationDamper"] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_chaser: List["PositionChaser"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_chaser2_d: List["PositionChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_damper: List["PositionDamper"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    position_damper2_d: List["PositionDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    scalar_chaser: List["ScalarChaser"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    scalar_damper: List["ScalarDamper"] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    tex_coord_chaser2_d: List["TexCoordChaser2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    tex_coord_damper2_d: List["TexCoordDamper2D"] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    texture_background: List["TextureBackground"] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    collidable_shape: List["CollidableShape"] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    collision_sensor: List["CollisionSensor"] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    rigid_body_collection: List["RigidBodyCollection"] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    particle_system: List["ParticleSystem"] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    transform_sensor: List["TransformSensor"] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    iso_surface_volume_data: List["IsoSurfaceVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    segmented_volume_data: List["SegmentedVolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    volume_data: List["VolumeData"] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    disentity_manager: List["DisentityManager"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    hanim_humanoid: List["HanimHumanoid"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    hanim_segment: List["HanimSegment"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    hanim_site: List["HanimSite"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    nurbs_orientation_interpolator: List["NurbsOrientationInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    nurbs_position_interpolator: List["NurbsPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    nurbs_surface_interpolator: List["NurbsSurfaceInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "ROUTE",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    extern_proto_declare: List[ExternProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ExternProtoDeclare",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    proto_declare: List[ProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ProtoDeclare",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "IMPORT",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    export: List[Export] = field(
        default_factory=list,
        metadata={
            "name": "EXPORT",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )


@dataclass
class X3DinfoNode(X3DchildNode):
    class Meta:
        name = "X3DInfoNode"


@dataclass
class X3DinterpolatorNode(X3DchildNode):
    class Meta:
        name = "X3DInterpolatorNode"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )


@dataclass
class X3DlayoutNode(X3DchildNode):
    class Meta:
        name = "X3DLayoutNode"


@dataclass
class X3DlightNode(X3DchildNode):
    class Meta:
        name = "X3DLightNode"

    ambient_intensity: float = field(
        default=0.0,
        metadata={
            "name": "ambientIntensity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    color: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    intensity: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    on: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DmaterialNode(X3DappearanceChildNode):
    class Meta:
        name = "X3DMaterialNode"


@dataclass
class X3DnbodyCollidableNode(X3DchildNode):
    class Meta:
        name = "X3DNBodyCollidableNode"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )


@dataclass
class X3DnormalNode(X3DgeometricPropertyNode):
    class Meta:
        name = "X3DNormalNode"


@dataclass
class X3DparametricGeometryNode(X3DgeometryNode):
    class Meta:
        name = "X3DParametricGeometryNode"


@dataclass
class X3DproductStructureChildNode(X3DchildNode):
    class Meta:
        name = "X3DProductStructureChildNode"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DprogrammableShaderObject:
    class Meta:
        name = "X3DProgrammableShaderObject"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_boolean: Optional[MetadataBoolean] = field(
        default=None,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_double: Optional[MetadataDouble] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_float: Optional[MetadataFloat] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_integer: Optional[MetadataInteger] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_set: Optional[MetadataSet] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    metadata_string: Optional[MetadataString] = field(
        default=None,
        metadata={
            "name": "MetadataString",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    def_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEF",
            "type": "Attribute",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "name": "USE",
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class X3DsensorNode(X3DchildNode):
    class Meta:
        name = "X3DSensorNode"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DsequencerNode(X3DchildNode):
    class Meta:
        name = "X3DSequencerNode"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )


@dataclass
class X3DshaderNode(X3DappearanceChildNode):
    class Meta:
        name = "X3DShaderNode"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DshapeNode(X3DchildNode):
    """
    :ivar appearance: appearance
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar bbox_center:
    :ivar bbox_size:
    """
    class Meta:
        name = "X3DShapeNode"

    appearance: List["Appearance"] = field(
        default_factory=list,
        metadata={
            "name": "Appearance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    box: List["Box"] = field(
        default_factory=list,
        metadata={
            "name": "Box",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    cone: List["Cone"] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    cylinder: List["Cylinder"] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_face_set: List["IndexedFaceSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_line_set: List["IndexedLineSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_triangle_fan_set: List["IndexedTriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_triangle_set: List["IndexedTriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_triangle_strip_set: List["IndexedTriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    line_set: List["LineSet"] = field(
        default_factory=list,
        metadata={
            "name": "LineSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    point_set: List["PointSet"] = field(
        default_factory=list,
        metadata={
            "name": "PointSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    sphere: List["Sphere"] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    triangle_fan_set: List["TriangleFanSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    triangle_set: List["TriangleSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    triangle_strip_set: List["TriangleStripSet"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    elevation_grid: List["ElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    polyline2_d: List["Polyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    polypoint2_d: List["Polypoint2D"] = field(
        default_factory=list,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    rectangle2_d: List["Rectangle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    triangle_set2_d: List["TriangleSet2D"] = field(
        default_factory=list,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    extrusion: List["Extrusion"] = field(
        default_factory=list,
        metadata={
            "name": "Extrusion",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    text: List["Text"] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    arc2_d: List["Arc2D"] = field(
        default_factory=list,
        metadata={
            "name": "Arc2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    arc_close2_d: List["ArcClose2D"] = field(
        default_factory=list,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    circle2_d: List["Circle2D"] = field(
        default_factory=list,
        metadata={
            "name": "Circle2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    disk2_d: List["Disk2D"] = field(
        default_factory=list,
        metadata={
            "name": "Disk2D",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    quad_set: List["QuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "QuadSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    indexed_quad_set: List["IndexedQuadSet"] = field(
        default_factory=list,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    geo_elevation_grid: List["GeoElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    nurbs_curve: List["NurbsCurve"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )


@dataclass
class X3DsoundNode(X3DchildNode):
    class Meta:
        name = "X3DSoundNode"


@dataclass
class X3DtextureCoordinateNode(X3DgeometricPropertyNode):
    class Meta:
        name = "X3DTextureCoordinateNode"


@dataclass
class X3DtextureNode(X3DappearanceChildNode):
    class Meta:
        name = "X3DTextureNode"


@dataclass
class X3DtextureTransformNode(X3DappearanceChildNode):
    class Meta:
        name = "X3DTextureTransformNode"


@dataclass
class X3DtimeDependentNode(X3DchildNode):
    class Meta:
        name = "X3DTimeDependentNode"

    loop: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    pause_time: float = field(
        default=0.0,
        metadata={
            "name": "pauseTime",
            "type": "Attribute",
        }
    )
    resume_time: float = field(
        default=0.0,
        metadata={
            "name": "resumeTime",
            "type": "Attribute",
        }
    )
    start_time: float = field(
        default=0.0,
        metadata={
            "name": "startTime",
            "type": "Attribute",
        }
    )
    stop_time: float = field(
        default=0.0,
        metadata={
            "name": "stopTime",
            "type": "Attribute",
        }
    )


@dataclass
class X3DtriggerNode(X3DchildNode):
    class Meta:
        name = "X3DTriggerNode"


@dataclass
class X3DvertexAttributeNode(X3DgeometricPropertyNode):
    class Meta:
        name = "X3DVertexAttributeNode"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DvolumeDataNode(X3DchildNode):
    class Meta:
        name = "X3DVolumeDataNode"

    dimensions: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )


@dataclass
class Anchor(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    parameter: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3DurlObject = field(
        default=ContainerFieldChoicesX3DurlObject.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Billboard(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    axis_of_rotation: str = field(
        default="0 1 0",
        metadata={
            "name": "axisOfRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BlendedVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar image_texture:
    :ivar pixel_texture:
    :ivar movie_texture:
    :ivar blended_volume_style:
    :ivar boundary_enhancement_volume_style:
    :ivar cartoon_volume_style:
    :ivar composed_volume_style:
    :ivar edge_enhancement_volume_style:
    :ivar opacity_map_volume_style:
    :ivar projection_volume_style:
    :ivar shaded_volume_style:
    :ivar silhouette_enhancement_volume_style:
    :ivar tone_mapped_volume_style:
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar weight_constant1:
    :ivar weight_constant2:
    :ivar weight_function1:
    :ivar weight_function2:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    blended_volume_style: List["BlendedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BlendedVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    boundary_enhancement_volume_style: List["BoundaryEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    cartoon_volume_style: List["CartoonVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "CartoonVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    composed_volume_style: List["ComposedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    edge_enhancement_volume_style: List["EdgeEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "EdgeEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    opacity_map_volume_style: List["OpacityMapVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "OpacityMapVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    projection_volume_style: List["ProjectionVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    shaded_volume_style: List["ShadedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ShadedVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    silhouette_enhancement_volume_style: List["SilhouetteEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "SilhouetteEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    tone_mapped_volume_style: List["ToneMappedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ToneMappedVolumeStyle",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    weight_constant1: float = field(
        default=0.5,
        metadata={
            "name": "weightConstant1",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    weight_constant2: float = field(
        default=0.5,
        metadata={
            "name": "weightConstant2",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    weight_function1: VolumeRenderingWeightFunctionChoices = field(
        default=VolumeRenderingWeightFunctionChoices.CONSTANT,
        metadata={
            "name": "weightFunction1",
            "type": "Attribute",
        }
    )
    weight_function2: VolumeRenderingWeightFunctionChoices = field(
        default=VolumeRenderingWeightFunctionChoices.CONSTANT,
        metadata={
            "name": "weightFunction2",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BooleanSequencer(X3DsequencerNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BooleanTrigger(X3DtriggerNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class BoundaryEnhancementVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    boundary_opacity: float = field(
        default=0.9,
        metadata={
            "name": "boundaryOpacity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    opacity_factor: float = field(
        default=2.0,
        metadata={
            "name": "opacityFactor",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    retained_opacity: float = field(
        default=0.2,
        metadata={
            "name": "retainedOpacity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cadassembly(X3DgroupingNode):
    class Meta:
        name = "CADAssembly"
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cadface(X3DproductStructureChildNode):
    """
    :ivar shape:
    :ivar lod:
    :ivar transform:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        name = "CADFace"
        namespace = "http://www.design2machine.com"

    shape: Optional["Shape"] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    lod: Optional["Lod"] = field(
        default=None,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    transform: Optional["Transform"] = field(
        default=None,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cadlayer(X3DgroupingNode):
    class Meta:
        name = "CADLayer"
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    visible: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Cadpart(X3DproductStructureChildNode):
    """
    :ivar cadface:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar center:
    :ivar rotation:
    :ivar scale:
    :ivar scale_orientation:
    :ivar translation:
    :ivar bbox_center:
    :ivar bbox_size:
    :ivar container_field:
    """
    class Meta:
        name = "CADPart"
        namespace = "http://www.design2machine.com"

    cadface: List["Cadface"] = field(
        default_factory=list,
        metadata={
            "name": "CADFace",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CartoonVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar color_steps:
    :ivar orthogonal_color:
    :ivar parallel_color:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: Optional["ComposedTexture3D"] = field(
        default=None,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: Optional["ImageTexture3D"] = field(
        default=None,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: Optional["PixelTexture3D"] = field(
        default=None,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    color_steps: int = field(
        default=4,
        metadata={
            "name": "colorSteps",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 64,
        }
    )
    orthogonal_color: str = field(
        default="1 1 1 1",
        metadata={
            "name": "orthogonalColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    parallel_color: str = field(
        default="0 0 0 1",
        metadata={
            "name": "parallelColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CollidableOffset(X3DnbodyCollidableNode):
    """
    :ivar collidable_offset: collidable
    :ivar collidable_shape: collidable
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    collidable_offset: Optional["CollidableOffset"] = field(
        default=None,
        metadata={
            "name": "CollidableOffset",
            "type": "Element",
        }
    )
    collidable_shape: Optional["CollidableShape"] = field(
        default=None,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CollidableShape(X3DnbodyCollidableNode):
    """
    :ivar shape: shape
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    shape: Optional["Shape"] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Collision(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CollisionSensor(X3DsensorNode):
    """
    :ivar collision_collection:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    collision_collection: Optional["CollisionCollection"] = field(
        default=None,
        metadata={
            "name": "CollisionCollection",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Color(X3DcolorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    color: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*((([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesColor = field(
        default=ContainerFieldChoicesColor.COLOR,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ColorInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*((([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ColorRgba(X3DcolorNode):
    class Meta:
        name = "ColorRGBA"
        namespace = "http://www.design2machine.com"

    color: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*((([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesColor = field(
        default=ContainerFieldChoicesColor.COLOR,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ComposedVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar blended_volume_style:
    :ivar boundary_enhancement_volume_style:
    :ivar cartoon_volume_style:
    :ivar composed_volume_style:
    :ivar edge_enhancement_volume_style:
    :ivar opacity_map_volume_style:
    :ivar projection_volume_style:
    :ivar shaded_volume_style:
    :ivar silhouette_enhancement_volume_style:
    :ivar tone_mapped_volume_style:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    blended_volume_style: List["BlendedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BlendedVolumeStyle",
            "type": "Element",
        }
    )
    boundary_enhancement_volume_style: List["BoundaryEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    cartoon_volume_style: List["CartoonVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "CartoonVolumeStyle",
            "type": "Element",
        }
    )
    composed_volume_style: List["ComposedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedVolumeStyle",
            "type": "Element",
        }
    )
    edge_enhancement_volume_style: List["EdgeEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "EdgeEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    opacity_map_volume_style: List["OpacityMapVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "OpacityMapVolumeStyle",
            "type": "Element",
        }
    )
    projection_volume_style: List["ProjectionVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionVolumeStyle",
            "type": "Element",
        }
    )
    shaded_volume_style: List["ShadedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ShadedVolumeStyle",
            "type": "Element",
        }
    )
    silhouette_enhancement_volume_style: List["SilhouetteEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "SilhouetteEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    tone_mapped_volume_style: List["ToneMappedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ToneMappedVolumeStyle",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Coordinate(X3DcoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesX3DcoordinateNode = field(
        default=ContainerFieldChoicesX3DcoordinateNode.COORD,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateDouble(X3DcoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesX3DcoordinateNode = field(
        default=ContainerFieldChoicesX3DcoordinateNode.COORD,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateInterpolator2D(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class DisentityTypeMapping(X3DinfoNode):
    class Meta:
        name = "DISEntityTypeMapping"
        namespace = "http://www.design2machine.com"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    category: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    country: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 65535,
        }
    )
    domain: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    extra: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    kind: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    specific: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    subcategory: int = field(
        default=0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 255,
        }
    )
    container_field: ContainerFieldChoicesDisentityTypeMapping = field(
        default=ContainerFieldChoicesDisentityTypeMapping.MAPPING,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class DirectionalLight(X3DlightNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    direction: str = field(
        default="0 0 -1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    global_value: bool = field(
        default=False,
        metadata={
            "name": "global",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class EdgeEnhancementVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar edge_color:
    :ivar gradient_threshold:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: Optional["ComposedTexture3D"] = field(
        default=None,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: Optional["ImageTexture3D"] = field(
        default=None,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: Optional["PixelTexture3D"] = field(
        default=None,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    edge_color: str = field(
        default="0 0 0 1",
        metadata={
            "name": "edgeColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    gradient_threshold: float = field(
        default=0.4,
        metadata={
            "name": "gradientThreshold",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 3.1416,
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class EspduTransform(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    marking: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    site_id: int = field(
        default=0,
        metadata={
            "name": "siteID",
            "type": "Attribute",
        }
    )
    application_id: int = field(
        default=0,
        metadata={
            "name": "applicationID",
            "type": "Attribute",
        }
    )
    entity_id: int = field(
        default=0,
        metadata={
            "name": "entityID",
            "type": "Attribute",
        }
    )
    force_id: int = field(
        default=0,
        metadata={
            "name": "forceID",
            "type": "Attribute",
        }
    )
    entity_kind: int = field(
        default=0,
        metadata={
            "name": "entityKind",
            "type": "Attribute",
        }
    )
    entity_domain: int = field(
        default=0,
        metadata={
            "name": "entityDomain",
            "type": "Attribute",
        }
    )
    entity_country: int = field(
        default=0,
        metadata={
            "name": "entityCountry",
            "type": "Attribute",
        }
    )
    entity_category: int = field(
        default=0,
        metadata={
            "name": "entityCategory",
            "type": "Attribute",
        }
    )
    entity_subcategory: int = field(
        default=0,
        metadata={
            "name": "entitySubcategory",
            "type": "Attribute",
        }
    )
    entity_specific: int = field(
        default=0,
        metadata={
            "name": "entitySpecific",
            "type": "Attribute",
        }
    )
    entity_extra: int = field(
        default=0,
        metadata={
            "name": "entityExtra",
            "type": "Attribute",
        }
    )
    read_interval: float = field(
        default=0.1,
        metadata={
            "name": "readInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    write_interval: float = field(
        default=1.0,
        metadata={
            "name": "writeInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    network_mode: NetworkModeChoices = field(
        default=NetworkModeChoices.STAND_ALONE,
        metadata={
            "name": "networkMode",
            "type": "Attribute",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    address: str = field(
        default="localhost",
        metadata={
            "type": "Attribute",
        }
    )
    port: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    multicast_relay_host: Optional[str] = field(
        default=None,
        metadata={
            "name": "multicastRelayHost",
            "type": "Attribute",
        }
    )
    multicast_relay_port: int = field(
        default=0,
        metadata={
            "name": "multicastRelayPort",
            "type": "Attribute",
        }
    )
    rtp_header_expected: bool = field(
        default=False,
        metadata={
            "name": "rtpHeaderExpected",
            "type": "Attribute",
        }
    )
    dead_reckoning: int = field(
        default=0,
        metadata={
            "name": "deadReckoning",
            "type": "Attribute",
        }
    )
    linear_velocity: str = field(
        default="0 0 0",
        metadata={
            "name": "linearVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    linear_acceleration: str = field(
        default="0 0 0",
        metadata={
            "name": "linearAcceleration",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    fired1: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    fired2: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    collision_type: int = field(
        default=0,
        metadata={
            "name": "collisionType",
            "type": "Attribute",
        }
    )
    detonation_location: str = field(
        default="0 0 0",
        metadata={
            "name": "detonationLocation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    detonation_relative_location: str = field(
        default="0 0 0",
        metadata={
            "name": "detonationRelativeLocation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    detonation_result: int = field(
        default=0,
        metadata={
            "name": "detonationResult",
            "type": "Attribute",
        }
    )
    event_application_id: int = field(
        default=0,
        metadata={
            "name": "eventApplicationID",
            "type": "Attribute",
        }
    )
    event_entity_id: int = field(
        default=0,
        metadata={
            "name": "eventEntityID",
            "type": "Attribute",
        }
    )
    event_number: int = field(
        default=0,
        metadata={
            "name": "eventNumber",
            "type": "Attribute",
        }
    )
    event_site_id: int = field(
        default=0,
        metadata={
            "name": "eventSiteID",
            "type": "Attribute",
        }
    )
    munition_start_point: str = field(
        default="0 0 0",
        metadata={
            "name": "munitionStartPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    munition_end_point: str = field(
        default="0 0 0",
        metadata={
            "name": "munitionEndPoint",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    munition_site_id: int = field(
        default=0,
        metadata={
            "name": "munitionSiteID",
            "type": "Attribute",
        }
    )
    munition_application_id: int = field(
        default=0,
        metadata={
            "name": "munitionApplicationID",
            "type": "Attribute",
        }
    )
    munition_entity_id: int = field(
        default=0,
        metadata={
            "name": "munitionEntityID",
            "type": "Attribute",
        }
    )
    fire_mission_index: int = field(
        default=0,
        metadata={
            "name": "fireMissionIndex",
            "type": "Attribute",
        }
    )
    warhead: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    fuse: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    munition_quantity: int = field(
        default=0,
        metadata={
            "name": "munitionQuantity",
            "type": "Attribute",
        }
    )
    firing_rate: int = field(
        default=0,
        metadata={
            "name": "firingRate",
            "type": "Attribute",
        }
    )
    firing_range: float = field(
        default=0.0,
        metadata={
            "name": "firingRange",
            "type": "Attribute",
        }
    )
    articulation_parameter_count: int = field(
        default=0,
        metadata={
            "name": "articulationParameterCount",
            "type": "Attribute",
        }
    )
    articulation_parameter_designator_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "articulationParameterDesignatorArray",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    articulation_parameter_change_indicator_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "articulationParameterChangeIndicatorArray",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    articulation_parameter_id_part_attached_to_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "articulationParameterIdPartAttachedToArray",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    articulation_parameter_type_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "articulationParameterTypeArray",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    articulation_parameter_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "articulationParameterArray",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class FloatVertexAttribute(X3DvertexAttributeNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    num_components: int = field(
        default=4,
        metadata={
            "name": "numComponents",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 4,
        }
    )
    container_field: str = field(
        default="attrib",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Fog(X3DbindableNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    color: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    fog_type: FogTypeChoices = field(
        default=FogTypeChoices.LINEAR,
        metadata={
            "name": "fogType",
            "type": "Attribute",
        }
    )
    visibility_range: float = field(
        default=0.0,
        metadata={
            "name": "visibilityRange",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoCoordinate(X3DcoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="coord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoLocation(X3DgroupingNode):
    """
    :ivar geo_origin: geoOrigin SFNode
    :ivar geo_system:
    :ivar geo_coords:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoMetadata(X3DinfoNode):
    """
    :ivar geo_coordinate:
    :ivar geo_elevation_grid:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_transform:
    :ivar geo_viewpoint:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar url:
    :ivar summary:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_coordinate: List["GeoCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "GeoCoordinate",
            "type": "Element",
        }
    )
    geo_elevation_grid: List["GeoElevationGrid"] = field(
        default_factory=list,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_position_interpolator: List["GeoPositionInterpolator"] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List["GeoProximitySensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List["GeoTouchSensor"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    geo_viewpoint: List["GeoViewpoint"] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    summary: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3DurlObject = field(
        default=ContainerFieldChoicesX3DurlObject.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoPositionInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoTransform(X3DgroupingNode):
    """
    :ivar geo_origin: geoOrigin SFNode
    :ivar geo_center:
    :ivar geo_system:
    :ivar rotation:
    :ivar scale:
    :ivar scale_orientation:
    :ivar translation:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_center: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Group(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: ContainerFieldChoicesGroupLodshapeTransform = field(
        default=ContainerFieldChoicesGroupLodshapeTransform.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class HanimSegment(X3DgroupingNode):
    class Meta:
        name = "HAnimSegment"
        namespace = "http://www.design2machine.com"

    hanim_displacer: List["HanimDisplacer"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimDisplacer",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mass: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    center_of_mass: str = field(
        default="0 0 0",
        metadata={
            "name": "centerOfMass",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    moments_of_inertia: str = field(
        default="0 0 0 0 0 0 0 0 0",
        metadata={
            "name": "momentsOfInertia",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesHanimSegment = field(
        default=ContainerFieldChoicesHanimSegment.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class HanimSite(X3DgroupingNode):
    class Meta:
        name = "HAnimSite"
        namespace = "http://www.design2machine.com"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: ContainerFieldChoicesHanimSite = field(
        default=ContainerFieldChoicesHanimSite.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedFaceSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    convex: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    crease_angle: float = field(
        default=0.0,
        metadata={
            "name": "creaseAngle",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    color_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "colorIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "coordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    normal_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "normalIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    tex_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "texCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedQuadSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    index: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedTriangleFanSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    index: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedTriangleSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    index: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IndexedTriangleStripSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    index: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IntegerSequencer(X3DsequencerNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IntegerTrigger(X3DtriggerNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    integer_key: int = field(
        default=-1,
        metadata={
            "name": "integerKey",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class IsoSurfaceVolumeData(X3DvolumeDataNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar blended_volume_style:
    :ivar boundary_enhancement_volume_style:
    :ivar cartoon_volume_style:
    :ivar composed_volume_style:
    :ivar edge_enhancement_volume_style:
    :ivar opacity_map_volume_style:
    :ivar projection_volume_style:
    :ivar shaded_volume_style:
    :ivar silhouette_enhancement_volume_style:
    :ivar tone_mapped_volume_style:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar contour_step_size:
    :ivar surface_tolerance:
    :ivar surface_values:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    blended_volume_style: List["BlendedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BlendedVolumeStyle",
            "type": "Element",
        }
    )
    boundary_enhancement_volume_style: List["BoundaryEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    cartoon_volume_style: List["CartoonVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "CartoonVolumeStyle",
            "type": "Element",
        }
    )
    composed_volume_style: List["ComposedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedVolumeStyle",
            "type": "Element",
        }
    )
    edge_enhancement_volume_style: List["EdgeEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "EdgeEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    opacity_map_volume_style: List["OpacityMapVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "OpacityMapVolumeStyle",
            "type": "Element",
        }
    )
    projection_volume_style: List["ProjectionVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionVolumeStyle",
            "type": "Element",
        }
    )
    shaded_volume_style: List["ShadedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ShadedVolumeStyle",
            "type": "Element",
        }
    )
    silhouette_enhancement_volume_style: List["SilhouetteEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "SilhouetteEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    tone_mapped_volume_style: List["ToneMappedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ToneMappedVolumeStyle",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    contour_step_size: float = field(
        default=0.0,
        metadata={
            "name": "contourStepSize",
            "type": "Attribute",
        }
    )
    surface_tolerance: float = field(
        default=0.0,
        metadata={
            "name": "surfaceTolerance",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    surface_values: Optional[str] = field(
        default=None,
        metadata={
            "name": "surfaceValues",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Lod(X3DgroupingNode):
    class Meta:
        name = "LOD"
        namespace = "http://www.design2machine.com"

    force_transitions: bool = field(
        default=False,
        metadata={
            "name": "forceTransitions",
            "type": "Attribute",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    range: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesGroupLodshapeTransform = field(
        default=ContainerFieldChoicesGroupLodshapeTransform.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Layout(X3DlayoutNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    align: LayoutAlignChoices = field(
        default=LayoutAlignChoices.CENTER_CENTER,
        metadata={
            "type": "Attribute",
        }
    )
    offset: str = field(
        default="0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    offset_units: LayoutUnitsChoices = field(
        default=LayoutUnitsChoices.WORLD_WORLD,
        metadata={
            "name": "offsetUnits",
            "type": "Attribute",
        }
    )
    scale_mode: LayoutScaleModeChoices = field(
        default=LayoutScaleModeChoices.NONE_NONE,
        metadata={
            "name": "scaleMode",
            "type": "Attribute",
        }
    )
    size: str = field(
        default="1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    size_units: LayoutUnitsChoices = field(
        default=LayoutUnitsChoices.WORLD_WORLD,
        metadata={
            "name": "sizeUnits",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="layout",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Material(X3DmaterialNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    ambient_intensity: float = field(
        default=0.2,
        metadata={
            "name": "ambientIntensity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    diffuse_color: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "diffuseColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    emissive_color: str = field(
        default="0 0 0",
        metadata={
            "name": "emissiveColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    shininess: float = field(
        default=0.2,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    specular_color: str = field(
        default="0 0 0",
        metadata={
            "name": "specularColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    transparency: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    container_field: str = field(
        default="material",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Matrix3VertexAttribute(X3DvertexAttributeNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){8}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="attrib",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Matrix4VertexAttribute(X3DvertexAttributeNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){15}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="attrib",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MultiTexture(X3DtextureNode):
    """
    :ivar image_texture:
    :ivar movie_texture:
    :ivar pixel_texture:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar alpha:
    :ivar color:
    :ivar function:
    :ivar mode:
    :ivar source:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    alpha: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    color: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    function: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    mode: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    source: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture2Dnode = field(
        default=ContainerFieldChoicesX3Dtexture2Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MultiTextureCoordinate(X3DtextureCoordinateNode):
    """
    :ivar texture_coordinate:
    :ivar texture_coordinate_generator:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    texture_coordinate_generator: List["TextureCoordinateGenerator"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="texCoord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MultiTextureTransform(X3DtextureTransformNode):
    """
    :ivar texture_transform:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    texture_transform: List["TextureTransform"] = field(
        default_factory=list,
        metadata={
            "name": "TextureTransform",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="textureTransform",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NavigationInfo(X3DbindableNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    avatar_size: str = field(
        default="0.25 1.6 0.75",
        metadata={
            "name": "avatarSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    headlight: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    speed: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    transition_time: float = field(
        default=1.0,
        metadata={
            "name": "transitionTime",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    transition_type: List[str] = field(
        default_factory=lambda: [
            "\"LINEAR\"",
        ],
        metadata={
            "name": "transitionType",
            "type": "Attribute",
            "tokens": True,
        }
    )
    type: List[str] = field(
        default_factory=lambda: [
            "\"EXAMINE\"",
            "\"ANY\"",
        ],
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    visibility_limit: float = field(
        default=0.0,
        metadata={
            "name": "visibilityLimit",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Normal(X3DnormalNode):
    """
    :ivar vector: Note: range [-1..1] required but not enforced since it
        produces false positives
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    vector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesX3DnormalNode = field(
        default=ContainerFieldChoicesX3DnormalNode.NORMAL,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NormalInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsCurve(X3DparametricGeometryNode):
    """
    :ivar coordinate:
    :ivar coordinate_double:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar closed:
    :ivar knot:
    :ivar order:
    :ivar tessellation:
    :ivar weight:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: Optional["Coordinate"] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: Optional["CoordinateDouble"] = field(
        default=None,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    closed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    knot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    order: int = field(
        default=3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    tessellation: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsSweptSurface(X3DparametricGeometryNode):
    """
    :ivar contour_polyline2_d: crossSectionCurve
    :ivar nurbs_curve2_d: crossSectionCurve
    :ivar nurbs_curve: trajectoryCurve
    :ivar proto_instance: Appropriately typed substitution node
    :ivar ccw:
    :ivar solid:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    nurbs_curve2_d: List["NurbsCurve2D"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve2D",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    nurbs_curve: List["NurbsCurve"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsSwungSurface(X3DparametricGeometryNode):
    """
    :ivar contour_polyline2_d:
    :ivar nurbs_curve2_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar ccw:
    :ivar solid:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    contour_polyline2_d: List["ContourPolyline2D"] = field(
        default_factory=list,
        metadata={
            "name": "ContourPolyline2D",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    nurbs_curve2_d: List["NurbsCurve2D"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsCurve2D",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    ccw: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class OpacityMapVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar image_texture:
    :ivar pixel_texture:
    :ivar movie_texture:
    :ivar multi_texture:
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: Optional["ImageTexture"] = field(
        default=None,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    pixel_texture: Optional["PixelTexture"] = field(
        default=None,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
        }
    )
    movie_texture: Optional["MovieTexture"] = field(
        default=None,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    multi_texture: Optional["MultiTexture"] = field(
        default=None,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
        }
    )
    composed_texture3_d: Optional["ComposedTexture3D"] = field(
        default=None,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: Optional["ImageTexture3D"] = field(
        default=None,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: Optional["PixelTexture3D"] = field(
        default=None,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class OrientationInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ParticleSystem(X3DshapeNode):
    """
    :ivar color: colorRamp
    :ivar color_rgba: colorRamp
    :ivar cone_emitter: emitter
    :ivar explosion_emitter: emitter
    :ivar point_emitter: emitter
    :ivar polyline_emitter: emitter
    :ivar surface_emitter: emitter
    :ivar volume_emitter: emitter
    :ivar bounded_physics_model: physics
    :ivar force_physics_model: physics
    :ivar wind_physics_model: physics
    :ivar texture_coordinate: texCoordRamp
    :ivar create_particles:
    :ivar enabled:
    :ivar lifetime_variation:
    :ivar max_particles:
    :ivar particle_lifetime:
    :ivar particle_size:
    :ivar color_key:
    :ivar geometry_type:
    :ivar tex_coord_key:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    color: Optional["Color"] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        }
    )
    color_rgba: Optional["ColorRgba"] = field(
        default=None,
        metadata={
            "name": "ColorRGBA",
            "type": "Element",
        }
    )
    cone_emitter: Optional["ConeEmitter"] = field(
        default=None,
        metadata={
            "name": "ConeEmitter",
            "type": "Element",
        }
    )
    explosion_emitter: Optional["ExplosionEmitter"] = field(
        default=None,
        metadata={
            "name": "ExplosionEmitter",
            "type": "Element",
        }
    )
    point_emitter: Optional["PointEmitter"] = field(
        default=None,
        metadata={
            "name": "PointEmitter",
            "type": "Element",
        }
    )
    polyline_emitter: Optional["PolylineEmitter"] = field(
        default=None,
        metadata={
            "name": "PolylineEmitter",
            "type": "Element",
        }
    )
    surface_emitter: Optional["SurfaceEmitter"] = field(
        default=None,
        metadata={
            "name": "SurfaceEmitter",
            "type": "Element",
        }
    )
    volume_emitter: Optional["VolumeEmitter"] = field(
        default=None,
        metadata={
            "name": "VolumeEmitter",
            "type": "Element",
        }
    )
    bounded_physics_model: List["BoundedPhysicsModel"] = field(
        default_factory=list,
        metadata={
            "name": "BoundedPhysicsModel",
            "type": "Element",
            "sequential": True,
        }
    )
    force_physics_model: List["ForcePhysicsModel"] = field(
        default_factory=list,
        metadata={
            "name": "ForcePhysicsModel",
            "type": "Element",
            "sequential": True,
        }
    )
    wind_physics_model: List["WindPhysicsModel"] = field(
        default_factory=list,
        metadata={
            "name": "WindPhysicsModel",
            "type": "Element",
            "sequential": True,
        }
    )
    texture_coordinate: Optional["TextureCoordinate"] = field(
        default=None,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    create_particles: bool = field(
        default=True,
        metadata={
            "name": "createParticles",
            "type": "Attribute",
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    lifetime_variation: float = field(
        default=0.25,
        metadata={
            "name": "lifetimeVariation",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    max_particles: int = field(
        default=200,
        metadata={
            "name": "maxParticles",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    particle_lifetime: float = field(
        default=5.0,
        metadata={
            "name": "particleLifetime",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    particle_size: str = field(
        default="0.02 0.02",
        metadata={
            "name": "particleSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    color_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "colorKey",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    geometry_type: ParticleSystemGeometryTypeValues = field(
        default=ParticleSystemGeometryTypeValues.QUAD,
        metadata={
            "name": "geometryType",
            "type": "Attribute",
        }
    )
    tex_coord_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "texCoordKey",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PickableGroup(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    nurbs_patch_surface: List["NurbsPatchSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_swept_surface: List["NurbsSweptSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_swung_surface: List["NurbsSwungSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_trimmed_surface: List["NurbsTrimmedSurface"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
            "sequential": True,
        }
    )
    object_type: List[str] = field(
        default_factory=lambda: [
            "\"ALL\"",
        ],
        metadata={
            "name": "objectType",
            "type": "Attribute",
            "tokens": True,
        }
    )
    pickable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PointLight(X3DlightNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    attenuation: str = field(
        default="1 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    location: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    radius: float = field(
        default=100.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    global_value: bool = field(
        default=True,
        metadata={
            "name": "global",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionInterpolator2D(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ProgramShader(X3DshaderNode):
    """
    :ivar shader_program:
    :ivar container_field: parent Appearance node
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    shader_program: List[ShaderProgram] = field(
        default_factory=list,
        metadata={
            "name": "ShaderProgram",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="shaders",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class QuadSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ScalarInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ScreenGroup(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SegmentedVolumeData(X3DvolumeDataNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar blended_volume_style:
    :ivar boundary_enhancement_volume_style:
    :ivar cartoon_volume_style:
    :ivar composed_volume_style:
    :ivar edge_enhancement_volume_style:
    :ivar opacity_map_volume_style:
    :ivar projection_volume_style:
    :ivar shaded_volume_style:
    :ivar silhouette_enhancement_volume_style:
    :ivar tone_mapped_volume_style:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar segment_enabled:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    blended_volume_style: List["BlendedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BlendedVolumeStyle",
            "type": "Element",
        }
    )
    boundary_enhancement_volume_style: List["BoundaryEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    cartoon_volume_style: List["CartoonVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "CartoonVolumeStyle",
            "type": "Element",
        }
    )
    composed_volume_style: List["ComposedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedVolumeStyle",
            "type": "Element",
        }
    )
    edge_enhancement_volume_style: List["EdgeEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "EdgeEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    opacity_map_volume_style: List["OpacityMapVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "OpacityMapVolumeStyle",
            "type": "Element",
        }
    )
    projection_volume_style: List["ProjectionVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionVolumeStyle",
            "type": "Element",
        }
    )
    shaded_volume_style: List["ShadedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ShadedVolumeStyle",
            "type": "Element",
        }
    )
    silhouette_enhancement_volume_style: List["SilhouetteEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "SilhouetteEnhancementVolumeStyle",
            "type": "Element",
        }
    )
    tone_mapped_volume_style: List["ToneMappedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ToneMappedVolumeStyle",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    segment_enabled: Optional[str] = field(
        default=None,
        metadata={
            "name": "segmentEnabled",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ShadedVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar material: material
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar lighting:
    :ivar shadows:
    :ivar phase_function:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    material: List["Material"] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    lighting: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    shadows: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    phase_function: str = field(
        default="Henyey-Greenstein",
        metadata={
            "name": "phaseFunction",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Shape(X3DshapeNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: ContainerFieldChoicesGroupLodshapeTransform = field(
        default=ContainerFieldChoicesGroupLodshapeTransform.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SilhouetteEnhancementVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar silhouette_boundary_opacity:
    :ivar silhouette_retained_opacity:
    :ivar silhouette_sharpness:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: Optional["ComposedTexture3D"] = field(
        default=None,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: Optional["ImageTexture3D"] = field(
        default=None,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: Optional["PixelTexture3D"] = field(
        default=None,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    silhouette_boundary_opacity: float = field(
        default=0.0,
        metadata={
            "name": "silhouetteBoundaryOpacity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    silhouette_retained_opacity: float = field(
        default=1.0,
        metadata={
            "name": "silhouetteRetainedOpacity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    silhouette_sharpness: float = field(
        default=0.5,
        metadata={
            "name": "silhouetteSharpness",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Sound(X3DsoundNode):
    """
    :ivar audio_clip:
    :ivar movie_texture:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar direction:
    :ivar intensity:
    :ivar location:
    :ivar max_back:
    :ivar max_front:
    :ivar min_back:
    :ivar min_front:
    :ivar priority:
    :ivar spatialize:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    audio_clip: Optional["AudioClip"] = field(
        default=None,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    movie_texture: Optional["MovieTexture"] = field(
        default=None,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    direction: str = field(
        default="0 0 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    intensity: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    location: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    max_back: float = field(
        default=10.0,
        metadata={
            "name": "maxBack",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    max_front: float = field(
        default=10.0,
        metadata={
            "name": "maxFront",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    min_back: float = field(
        default=1.0,
        metadata={
            "name": "minBack",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    min_front: float = field(
        default=1.0,
        metadata={
            "name": "minFront",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    priority: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    spatialize: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SplinePositionInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    closed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    key_velocity: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    normalize_velocity: bool = field(
        default=False,
        metadata={
            "name": "normalizeVelocity",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SplinePositionInterpolator2D(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    closed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    key_velocity: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    normalize_velocity: bool = field(
        default=False,
        metadata={
            "name": "normalizeVelocity",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SplineScalarInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    closed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    key_velocity: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyVelocity",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    normalize_velocity: bool = field(
        default=False,
        metadata={
            "name": "normalizeVelocity",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SpotLight(X3DlightNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    attenuation: str = field(
        default="1 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    beam_width: float = field(
        default=0.7854,
        metadata={
            "name": "beamWidth",
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1.570796,
        }
    )
    cut_off_angle: float = field(
        default=1.570796,
        metadata={
            "name": "cutOffAngle",
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1.570796,
        }
    )
    direction: str = field(
        default="0 0 -1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    location: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    radius: float = field(
        default=100.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    global_value: bool = field(
        default=True,
        metadata={
            "name": "global",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SquadOrientationInterpolator(X3DinterpolatorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    key_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    normalize_velocity: bool = field(
        default=False,
        metadata={
            "name": "normalizeVelocity",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Switch(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    which_choice: int = field(
        default=-1,
        metadata={
            "name": "whichChoice",
            "type": "Attribute",
            "min_inclusive": -1,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureCoordinate(X3DtextureCoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesTextureCoordinate = field(
        default=ContainerFieldChoicesTextureCoordinate.TEX_COORD,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureCoordinate3D(X3DtextureCoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="texCoord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureCoordinate4D(X3DtextureCoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="texCoord",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureCoordinateGenerator(X3DtextureCoordinateNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    mode: TextureCoordinateGeneratorModeChoices = field(
        default=TextureCoordinateGeneratorModeChoices.SPHERE,
        metadata={
            "type": "Attribute",
        }
    )
    parameter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesTextureCoordinate = field(
        default=ContainerFieldChoicesTextureCoordinate.TEX_COORD,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureTransform(X3DtextureTransformNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center: str = field(
        default="0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    scale: str = field(
        default="1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="textureTransform",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureTransform3D(X3DtextureTransformNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="textureTransform",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureTransformMatrix3D(X3DtextureTransformNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    matrix: str = field(
        default="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){15}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="textureTransform",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TimeSensor(X3DtimeDependentNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    cycle_interval: float = field(
        default=1.0,
        metadata={
            "name": "cycleInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    enabled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TimeTrigger(X3DtriggerNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ToneMappedVolumeStyle(X3DcomposableVolumeRenderStyleNode):
    """
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar cool_color:
    :ivar warm_color:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    composed_texture3_d: Optional["ComposedTexture3D"] = field(
        default=None,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
        }
    )
    image_texture3_d: Optional["ImageTexture3D"] = field(
        default=None,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    pixel_texture3_d: Optional["PixelTexture3D"] = field(
        default=None,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    cool_color: str = field(
        default="0 0 1 0",
        metadata={
            "name": "coolColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    warm_color: str = field(
        default="1 1 0 0",
        metadata={
            "name": "warmColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){3}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    container_field: str = field(
        default="renderStyle",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Transform(X3DgroupingNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    rotation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale: str = field(
        default="1 1 1",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    scale_orientation: str = field(
        default="0 0 1 0",
        metadata={
            "name": "scaleOrientation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    translation: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: ContainerFieldChoicesGroupLodshapeTransform = field(
        default=ContainerFieldChoicesGroupLodshapeTransform.CHILDREN,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TriangleFanSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    fan_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "fanCount",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TriangleSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TriangleStripSet(X3DcomposedGeometryNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    strip_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "stripCount",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TwoSidedMaterial(X3DmaterialNode):
    """
    Deprecated in X3D version 4.
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    ambient_intensity: float = field(
        default=0.2,
        metadata={
            "name": "ambientIntensity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    back_ambient_intensity: float = field(
        default=0.2,
        metadata={
            "name": "backAmbientIntensity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    diffuse_color: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "diffuseColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    back_diffuse_color: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "backDiffuseColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    emissive_color: str = field(
        default="0 0 0",
        metadata={
            "name": "emissiveColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    back_emissive_color: str = field(
        default="0 0 0",
        metadata={
            "name": "backEmissiveColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    shininess: float = field(
        default=0.2,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    back_shininess: float = field(
        default=0.2,
        metadata={
            "name": "backShininess",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    specular_color: str = field(
        default="0 0 0",
        metadata={
            "name": "specularColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    back_specular_color: str = field(
        default="0 0 0",
        metadata={
            "name": "backSpecularColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    transparency: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    back_transparency: float = field(
        default=0.0,
        metadata={
            "name": "backTransparency",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    separate_back_color: bool = field(
        default=False,
        metadata={
            "name": "separateBackColor",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="material",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class VolumeData(X3DvolumeDataNode):
    """
    :ivar blended_volume_style:
    :ivar boundary_enhancement_volume_style:
    :ivar cartoon_volume_style:
    :ivar composed_volume_style:
    :ivar edge_enhancement_volume_style:
    :ivar opacity_map_volume_style:
    :ivar projection_volume_style:
    :ivar shaded_volume_style:
    :ivar silhouette_enhancement_volume_style:
    :ivar tone_mapped_volume_style:
    :ivar composed_texture3_d:
    :ivar image_texture3_d:
    :ivar pixel_texture3_d:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    blended_volume_style: List["BlendedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BlendedVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    boundary_enhancement_volume_style: List["BoundaryEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    cartoon_volume_style: List["CartoonVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "CartoonVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    composed_volume_style: List["ComposedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    edge_enhancement_volume_style: List["EdgeEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "EdgeEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    opacity_map_volume_style: List["OpacityMapVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "OpacityMapVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    projection_volume_style: List["ProjectionVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    shaded_volume_style: List["ShadedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ShadedVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    silhouette_enhancement_volume_style: List["SilhouetteEnhancementVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "SilhouetteEnhancementVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    tone_mapped_volume_style: List["ToneMappedVolumeStyle"] = field(
        default_factory=list,
        metadata={
            "name": "ToneMappedVolumeStyle",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    composed_texture3_d: List["ComposedTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ComposedTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pixel_texture3_d: List["PixelTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture3D",
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class WorldInfo(X3DinfoNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    info: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3DbackgroundNode(X3DbindableNode):
    class Meta:
        name = "X3DBackgroundNode"

    ground_angle: Optional[str] = field(
        default=None,
        metadata={
            "name": "groundAngle",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    ground_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "groundColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*((([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    sky_angle: Optional[str] = field(
        default=None,
        metadata={
            "name": "skyAngle",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    sky_color: str = field(
        default="0 0 0",
        metadata={
            "name": "skyColor",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*((([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+-]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    transparency: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )


@dataclass
class X3DchaserNode(X3DfollowerNode):
    class Meta:
        name = "X3DChaserNode"

    duration: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )


@dataclass
class X3DdamperNode(X3DfollowerNode):
    class Meta:
        name = "X3DDamperNode"

    tau: float = field(
        default=0.3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    tolerance: float = field(
        default=-1.0,
        metadata={
            "type": "Attribute",
        }
    )
    order: int = field(
        default=3,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 5,
        }
    )


@dataclass
class X3DenvironmentTextureNode(X3DtextureNode):
    class Meta:
        name = "X3DEnvironmentTextureNode"


@dataclass
class X3DenvironmentalSensorNode(X3DsensorNode):
    class Meta:
        name = "X3DEnvironmentalSensorNode"

    size: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )


@dataclass
class X3DkeyDeviceSensorNode(X3DsensorNode):
    class Meta:
        name = "X3DKeyDeviceSensorNode"


@dataclass
class X3DnetworkSensorNode(X3DsensorNode):
    class Meta:
        name = "X3DNetworkSensorNode"


@dataclass
class X3DnurbsSurfaceGeometryNode(X3DparametricGeometryNode):
    class Meta:
        name = "X3DNurbsSurfaceGeometryNode"

    u_closed: bool = field(
        default=False,
        metadata={
            "name": "uClosed",
            "type": "Attribute",
        }
    )
    v_closed: bool = field(
        default=False,
        metadata={
            "name": "vClosed",
            "type": "Attribute",
        }
    )
    u_dimension: int = field(
        default=0,
        metadata={
            "name": "uDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    v_dimension: int = field(
        default=0,
        metadata={
            "name": "vDimension",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    u_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "uKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    v_knot: Optional[str] = field(
        default=None,
        metadata={
            "name": "vKnot",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    u_order: int = field(
        default=3,
        metadata={
            "name": "uOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    v_order: int = field(
        default=3,
        metadata={
            "name": "vOrder",
            "type": "Attribute",
            "min_inclusive": 2,
        }
    )
    u_tessellation: int = field(
        default=0,
        metadata={
            "name": "uTessellation",
            "type": "Attribute",
        }
    )
    v_tessellation: int = field(
        default=0,
        metadata={
            "name": "vTessellation",
            "type": "Attribute",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    solid: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DpickSensorNode(X3DsensorNode):
    class Meta:
        name = "X3DPickSensorNode"

    intersection_type: str = field(
        default="BOUNDS",
        metadata={
            "name": "intersectionType",
            "type": "Attribute",
        }
    )
    match_criterion: str = field(
        default="MATCH_ANY",
        metadata={
            "name": "matchCriterion",
            "type": "Attribute",
        }
    )
    object_type: List[str] = field(
        default_factory=lambda: [
            "\"ALL\"",
        ],
        metadata={
            "name": "objectType",
            "type": "Attribute",
            "tokens": True,
        }
    )
    sort_order: str = field(
        default="CLOSEST",
        metadata={
            "name": "sortOrder",
            "type": "Attribute",
        }
    )


@dataclass
class X3DpointingDeviceSensorNode(X3DsensorNode):
    class Meta:
        name = "X3DPointingDeviceSensorNode"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class X3DsoundSourceNode(X3DtimeDependentNode):
    class Meta:
        name = "X3DSoundSourceNode"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    pitch: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
        }
    )


@dataclass
class X3Dtexture2Dnode(X3DtextureNode):
    """
    :ivar texture_properties:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar repeat_s:
    :ivar repeat_t:
    """
    class Meta:
        name = "X3DTexture2DNode"

    texture_properties: Optional["TextureProperties"] = field(
        default=None,
        metadata={
            "name": "TextureProperties",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    repeat_s: bool = field(
        default=True,
        metadata={
            "name": "repeatS",
            "type": "Attribute",
        }
    )
    repeat_t: bool = field(
        default=True,
        metadata={
            "name": "repeatT",
            "type": "Attribute",
        }
    )


@dataclass
class X3Dtexture3Dnode(X3DtextureNode):
    """
    :ivar texture_properties:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar repeat_s:
    :ivar repeat_t:
    :ivar repeat_r:
    """
    class Meta:
        name = "X3DTexture3DNode"

    texture_properties: Optional["TextureProperties"] = field(
        default=None,
        metadata={
            "name": "TextureProperties",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    repeat_s: bool = field(
        default=False,
        metadata={
            "name": "repeatS",
            "type": "Attribute",
        }
    )
    repeat_t: bool = field(
        default=False,
        metadata={
            "name": "repeatT",
            "type": "Attribute",
        }
    )
    repeat_r: bool = field(
        default=False,
        metadata={
            "name": "repeatR",
            "type": "Attribute",
        }
    )


@dataclass
class X3DviewpointNode(X3DbindableNode):
    class Meta:
        name = "X3DViewpointNode"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    jump: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: str = field(
        default="0 0 1 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    retain_user_offsets: bool = field(
        default=False,
        metadata={
            "name": "retainUserOffsets",
            "type": "Attribute",
        }
    )


@dataclass
class X3DviewportNode(X3DgroupingNode):
    class Meta:
        name = "X3DViewportNode"


@dataclass
class AudioClip(X3DsoundSourceNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesAudioClip = field(
        default=ContainerFieldChoicesAudioClip.SOURCE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Background(X3DbackgroundNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    back_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "backUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    bottom_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "bottomUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    front_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "frontUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    left_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "leftUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    right_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "rightUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    top_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "topUrl",
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ColorChaser(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    initial_value: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ColorDamper(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    initial_value: str = field(
        default="0.8 0.8 0.8",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)+){2}([+]?((0(\.[0-9]*)?|\.[0-9]+)|1(\.0*)?)([Ee][+-]?[0-9]+)?)(\s)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ComposedCubeMapTexture(X3DenvironmentTextureNode):
    """
    :ivar image_texture:
    :ivar pixel_texture:
    :ivar movie_texture:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    container_field: str = field(
        default="texture",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ComposedTexture3D(X3Dtexture3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
            "sequential": True,
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
            "sequential": True,
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture3Dnode = field(
        default=ContainerFieldChoicesX3Dtexture3Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateChaser(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    initial_value: str = field(
        default="0 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateDamper(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    initial_value: str = field(
        default="0 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeneratedCubeMapTexture(X3DenvironmentTextureNode):
    """
    :ivar texture_properties:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar size:
    :ivar update:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    texture_properties: Optional["TextureProperties"] = field(
        default=None,
        metadata={
            "name": "TextureProperties",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    size: int = field(
        default=128,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0,
        }
    )
    update: GeneratedCubeMapTextureUpdateChoices = field(
        default=GeneratedCubeMapTextureUpdateChoices.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="texture",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoProximitySensor(X3DenvironmentalSensorNode):
    """
    :ivar geo_origin: geoOrigin SFNode
    :ivar center:
    :ivar geo_center:
    :ivar geo_system:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    geo_center: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoViewpoint(X3DviewpointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    center_of_rotation: str = field(
        default="0 0 0",
        metadata={
            "name": "centerOfRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    field_of_view: float = field(
        default=0.7854,
        metadata={
            "name": "fieldOfView",
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_exclusive": 3.1416,
        }
    )
    position: str = field(
        default="0 0 100000",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    speed_factor: float = field(
        default=1.0,
        metadata={
            "name": "speedFactor",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ImageCubeMapTexture(X3DenvironmentTextureNode):
    """
    :ivar texture_properties:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar url:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    texture_properties: Optional["TextureProperties"] = field(
        default=None,
        metadata={
            "name": "TextureProperties",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture2Dnode = field(
        default=ContainerFieldChoicesX3Dtexture2Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ImageTexture(X3Dtexture2Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3DUrlObjectTexture = field(
        default=ContainerFieldChoicesX3DUrlObjectTexture.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ImageTexture3D(X3Dtexture3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture3Dnode = field(
        default=ContainerFieldChoicesX3Dtexture3Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class KeySensor(X3DkeyDeviceSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LinePickSensor(X3DpickSensorNode):
    """
    :ivar line_set:
    :ivar indexed_line_set:
    :ivar anchor:
    :ivar billboard:
    :ivar collision:
    :ivar group:
    :ivar inline:
    :ivar lod:
    :ivar static_group:
    :ivar switch:
    :ivar transform:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_transform:
    :ivar hanim_joint:
    :ivar nurbs_set:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar viewport:
    :ivar layout_group:
    :ivar screen_group:
    :ivar shape:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    line_set: Optional["LineSet"] = field(
        default=None,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    indexed_line_set: Optional["IndexedLineSet"] = field(
        default=None,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "sequential": True,
        }
    )
    layout_group: List["LayoutGroup"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    screen_group: List["ScreenGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class LoadSensor(X3DnetworkSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    audio_clip: List["AudioClip"] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    disentity_type_mapping: List["DisentityTypeMapping"] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityTypeMapping",
            "type": "Element",
        }
    )
    geo_metadata: List["GeoMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    image_cube_map_texture: List["ImageCubeMapTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageCubeMapTexture",
            "type": "Element",
        }
    )
    image_texture3_d: List["ImageTexture3D"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture3D",
            "type": "Element",
        }
    )
    packaged_shader: List[PackagedShader] = field(
        default_factory=list,
        metadata={
            "name": "PackagedShader",
            "type": "Element",
        }
    )
    shader_part: List[ShaderPart] = field(
        default_factory=list,
        metadata={
            "name": "ShaderPart",
            "type": "Element",
        }
    )
    shader_program: List[ShaderProgram] = field(
        default_factory=list,
        metadata={
            "name": "ShaderProgram",
            "type": "Element",
        }
    )
    time_out: float = field(
        default=0.0,
        metadata={
            "name": "timeOut",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class MovieTexture(X3DsoundSourceNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    url: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    repeat_s: bool = field(
        default=True,
        metadata={
            "name": "repeatS",
            "type": "Attribute",
        }
    )
    repeat_t: bool = field(
        default=True,
        metadata={
            "name": "repeatT",
            "type": "Attribute",
        }
    )
    speed: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: ContainerFieldChoicesX3DUrlObjectTexture = field(
        default=ContainerFieldChoicesX3DUrlObjectTexture.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsPatchSurface(X3DnurbsSurfaceGeometryNode):
    """
    :ivar coordinate: controlPoint
    :ivar coordinate_double: controlPoint
    :ivar texture_coordinate: texCoord
    :ivar texture_coordinate_generator: texCoord
    :ivar nurbs_texture_coordinate: texCoord
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    texture_coordinate_generator: List["TextureCoordinateGenerator"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class NurbsTrimmedSurface(X3DnurbsSurfaceGeometryNode):
    """
    :ivar contour2_d: trimmingContour
    :ivar coordinate: controlPoint
    :ivar coordinate_double: controlPoint
    :ivar texture_coordinate: texCoord
    :ivar texture_coordinate_generator: texCoord
    :ivar nurbs_texture_coordinate: texCoord
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    contour2_d: List["Contour2D"] = field(
        default_factory=list,
        metadata={
            "name": "Contour2D",
            "type": "Element",
        }
    )
    coordinate: List["Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
        }
    )
    coordinate_double: List["CoordinateDouble"] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDouble",
            "type": "Element",
        }
    )
    texture_coordinate: List["TextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinate",
            "type": "Element",
        }
    )
    texture_coordinate_generator: List["TextureCoordinateGenerator"] = field(
        default_factory=list,
        metadata={
            "name": "TextureCoordinateGenerator",
            "type": "Element",
        }
    )
    nurbs_texture_coordinate: List["NurbsTextureCoordinate"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsTextureCoordinate",
            "type": "Element",
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class OrientationChaser(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 1 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 1 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class OrientationDamper(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 1 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 1 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class OrthoViewpoint(X3DviewpointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center_of_rotation: str = field(
        default="0 0 0",
        metadata={
            "name": "centerOfRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    field_of_view: str = field(
        default="-1 -1 1 1",
        metadata={
            "name": "fieldOfView",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    position: str = field(
        default="0 0 10",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PixelTexture(X3Dtexture2Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    image: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "min_length": 5,
            "white_space": "collapse",
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture2Dnode = field(
        default=ContainerFieldChoicesX3Dtexture2Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PixelTexture3D(X3Dtexture3Dnode):
    class Meta:
        namespace = "http://www.design2machine.com"

    image: str = field(
        default="0 0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    container_field: ContainerFieldChoicesX3Dtexture3Dnode = field(
        default=ContainerFieldChoicesX3Dtexture3Dnode.TEXTURE,
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PointPickSensor(X3DpickSensorNode):
    """
    :ivar point_set:
    :ivar anchor:
    :ivar billboard:
    :ivar collision:
    :ivar group:
    :ivar inline:
    :ivar lod:
    :ivar static_group:
    :ivar switch:
    :ivar transform:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_transform:
    :ivar hanim_joint:
    :ivar nurbs_set:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar viewport:
    :ivar layout_group:
    :ivar screen_group:
    :ivar shape:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    point_set: Optional["PointSet"] = field(
        default=None,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "sequential": True,
        }
    )
    layout_group: List["LayoutGroup"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    screen_group: List["ScreenGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionChaser(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionChaser2D(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionDamper(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PositionDamper2D(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: str = field(
        default="0 0",
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    initial_value: str = field(
        default="0 0",
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PrimitivePickSensor(X3DpickSensorNode):
    """
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar sphere:
    :ivar anchor:
    :ivar billboard:
    :ivar collision:
    :ivar group:
    :ivar inline:
    :ivar lod:
    :ivar static_group:
    :ivar switch:
    :ivar transform:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_transform:
    :ivar hanim_joint:
    :ivar nurbs_set:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar viewport:
    :ivar layout_group:
    :ivar screen_group:
    :ivar shape:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    box: Optional["Box"] = field(
        default=None,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: Optional["Cone"] = field(
        default=None,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: Optional["Cylinder"] = field(
        default=None,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    sphere: Optional["Sphere"] = field(
        default=None,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "sequential": True,
        }
    )
    layout_group: List["LayoutGroup"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    screen_group: List["ScreenGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ProximitySensor(X3DenvironmentalSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ReceiverPdu(X3DnetworkSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    which_geometry: int = field(
        default=1,
        metadata={
            "name": "whichGeometry",
            "type": "Attribute",
        }
    )
    read_interval: float = field(
        default=0.1,
        metadata={
            "name": "readInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    write_interval: float = field(
        default=1.0,
        metadata={
            "name": "writeInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    network_mode: NetworkModeChoices = field(
        default=NetworkModeChoices.STAND_ALONE,
        metadata={
            "name": "networkMode",
            "type": "Attribute",
        }
    )
    site_id: int = field(
        default=0,
        metadata={
            "name": "siteID",
            "type": "Attribute",
        }
    )
    application_id: int = field(
        default=0,
        metadata={
            "name": "applicationID",
            "type": "Attribute",
        }
    )
    entity_id: int = field(
        default=0,
        metadata={
            "name": "entityID",
            "type": "Attribute",
        }
    )
    address: str = field(
        default="localhost",
        metadata={
            "type": "Attribute",
        }
    )
    port: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    multicast_relay_host: Optional[str] = field(
        default=None,
        metadata={
            "name": "multicastRelayHost",
            "type": "Attribute",
        }
    )
    multicast_relay_port: int = field(
        default=0,
        metadata={
            "name": "multicastRelayPort",
            "type": "Attribute",
        }
    )
    rtp_header_expected: bool = field(
        default=False,
        metadata={
            "name": "rtpHeaderExpected",
            "type": "Attribute",
        }
    )
    radio_id: int = field(
        default=0,
        metadata={
            "name": "radioID",
            "type": "Attribute",
        }
    )
    received_power: float = field(
        default=0.0,
        metadata={
            "name": "receivedPower",
            "type": "Attribute",
        }
    )
    receiver_state: int = field(
        default=0,
        metadata={
            "name": "receiverState",
            "type": "Attribute",
        }
    )
    transmitter_site_id: int = field(
        default=0,
        metadata={
            "name": "transmitterSiteID",
            "type": "Attribute",
        }
    )
    transmitter_application_id: int = field(
        default=0,
        metadata={
            "name": "transmitterApplicationID",
            "type": "Attribute",
        }
    )
    transmitter_entity_id: int = field(
        default=0,
        metadata={
            "name": "transmitterEntityID",
            "type": "Attribute",
        }
    )
    transmitter_radio_id: int = field(
        default=0,
        metadata={
            "name": "transmitterRadioID",
            "type": "Attribute",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ScalarChaser(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: float = field(
        default=0.0,
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
        }
    )
    initial_value: float = field(
        default=0.0,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class ScalarDamper(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: float = field(
        default=0.0,
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
        }
    )
    initial_value: float = field(
        default=0.0,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SignalPdu(X3DnetworkSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    which_geometry: int = field(
        default=1,
        metadata={
            "name": "whichGeometry",
            "type": "Attribute",
        }
    )
    read_interval: float = field(
        default=0.1,
        metadata={
            "name": "readInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    write_interval: float = field(
        default=1.0,
        metadata={
            "name": "writeInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    network_mode: NetworkModeChoices = field(
        default=NetworkModeChoices.STAND_ALONE,
        metadata={
            "name": "networkMode",
            "type": "Attribute",
        }
    )
    site_id: int = field(
        default=0,
        metadata={
            "name": "siteID",
            "type": "Attribute",
        }
    )
    application_id: int = field(
        default=0,
        metadata={
            "name": "applicationID",
            "type": "Attribute",
        }
    )
    entity_id: int = field(
        default=0,
        metadata={
            "name": "entityID",
            "type": "Attribute",
        }
    )
    address: str = field(
        default="localhost",
        metadata={
            "type": "Attribute",
        }
    )
    port: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    multicast_relay_host: Optional[str] = field(
        default=None,
        metadata={
            "name": "multicastRelayHost",
            "type": "Attribute",
        }
    )
    multicast_relay_port: int = field(
        default=0,
        metadata={
            "name": "multicastRelayPort",
            "type": "Attribute",
        }
    )
    rtp_header_expected: bool = field(
        default=False,
        metadata={
            "name": "rtpHeaderExpected",
            "type": "Attribute",
        }
    )
    radio_id: int = field(
        default=0,
        metadata={
            "name": "radioID",
            "type": "Attribute",
        }
    )
    encoding_scheme: int = field(
        default=0,
        metadata={
            "name": "encodingScheme",
            "type": "Attribute",
        }
    )
    tdl_type: int = field(
        default=0,
        metadata={
            "name": "tdlType",
            "type": "Attribute",
        }
    )
    sample_rate: int = field(
        default=0,
        metadata={
            "name": "sampleRate",
            "type": "Attribute",
        }
    )
    samples: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    data_length: int = field(
        default=0,
        metadata={
            "name": "dataLength",
            "type": "Attribute",
        }
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class StringSensor(X3DkeyDeviceSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    deletion_allowed: bool = field(
        default=True,
        metadata={
            "name": "deletionAllowed",
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TexCoordChaser2D(X3DchaserNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TexCoordDamper2D(X3DdamperNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    initial_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialDestination",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TextureBackground(X3DbackgroundNode):
    """
    :ivar image_texture:
    :ivar movie_texture:
    :ivar multi_texture:
    :ivar pixel_texture:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    image_texture: List["ImageTexture"] = field(
        default_factory=list,
        metadata={
            "name": "ImageTexture",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    movie_texture: List["MovieTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MovieTexture",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    multi_texture: List["MultiTexture"] = field(
        default_factory=list,
        metadata={
            "name": "MultiTexture",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    pixel_texture: List["PixelTexture"] = field(
        default_factory=list,
        metadata={
            "name": "PixelTexture",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TransformSensor(X3DenvironmentalSensorNode):
    """
    :ivar anchor:
    :ivar billboard:
    :ivar collision:
    :ivar group:
    :ivar lod:
    :ivar shape:
    :ivar static_group:
    :ivar switch:
    :ivar transform:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_transform:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar pickable_group:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar center:
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    anchor: Optional["Anchor"] = field(
        default=None,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    billboard: Optional["Billboard"] = field(
        default=None,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: Optional["Collision"] = field(
        default=None,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    group: Optional["Group"] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    lod: Optional["Lod"] = field(
        default=None,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    shape: Optional["Shape"] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    static_group: Optional["StaticGroup"] = field(
        default=None,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    switch: Optional["Switch"] = field(
        default=None,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    transform: Optional["Transform"] = field(
        default=None,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    espdu_transform: Optional["EspduTransform"] = field(
        default=None,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: Optional["ReceiverPdu"] = field(
        default=None,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: Optional["SignalPdu"] = field(
        default=None,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: Optional["TransmitterPdu"] = field(
        default=None,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    cadassembly: Optional["Cadassembly"] = field(
        default=None,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: Optional["Cadlayer"] = field(
        default=None,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: Optional["Cadpart"] = field(
        default=None,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    geo_location: Optional["GeoLocation"] = field(
        default=None,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: Optional["GeoLod"] = field(
        default=None,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_transform: Optional["GeoTransform"] = field(
        default=None,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_joint: Optional["HanimJoint"] = field(
        default=None,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: Optional["HanimSegment"] = field(
        default=None,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: Optional["HanimSite"] = field(
        default=None,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    pickable_group: Optional["PickableGroup"] = field(
        default=None,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    proto_instance: Optional["ProtoInstance"] = field(
        default=None,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TransmitterPdu(X3DnetworkSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    bbox_center: str = field(
        default="0 0 0",
        metadata={
            "name": "bboxCenter",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    bbox_size: str = field(
        default="-1 -1 -1",
        metadata={
            "name": "bboxSize",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+]?(((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*)|((\-1(\.(0)*)?([Ee][+-]?[0]+)?\s+){2}\-1(\.(0)*)?([Ee][+-]?[0]+)?)\s*)?",
        }
    )
    which_geometry: int = field(
        default=1,
        metadata={
            "name": "whichGeometry",
            "type": "Attribute",
        }
    )
    read_interval: float = field(
        default=0.1,
        metadata={
            "name": "readInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    write_interval: float = field(
        default=1.0,
        metadata={
            "name": "writeInterval",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    network_mode: NetworkModeChoices = field(
        default=NetworkModeChoices.STAND_ALONE,
        metadata={
            "name": "networkMode",
            "type": "Attribute",
        }
    )
    site_id: int = field(
        default=0,
        metadata={
            "name": "siteID",
            "type": "Attribute",
        }
    )
    application_id: int = field(
        default=0,
        metadata={
            "name": "applicationID",
            "type": "Attribute",
        }
    )
    entity_id: int = field(
        default=0,
        metadata={
            "name": "entityID",
            "type": "Attribute",
        }
    )
    address: str = field(
        default="localhost",
        metadata={
            "type": "Attribute",
        }
    )
    port: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    multicast_relay_host: Optional[str] = field(
        default=None,
        metadata={
            "name": "multicastRelayHost",
            "type": "Attribute",
        }
    )
    multicast_relay_port: int = field(
        default=0,
        metadata={
            "name": "multicastRelayPort",
            "type": "Attribute",
        }
    )
    rtp_header_expected: bool = field(
        default=False,
        metadata={
            "name": "rtpHeaderExpected",
            "type": "Attribute",
        }
    )
    radio_id: int = field(
        default=0,
        metadata={
            "name": "radioID",
            "type": "Attribute",
        }
    )
    antenna_location: str = field(
        default="0 0 0",
        metadata={
            "name": "antennaLocation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    antenna_pattern_length: int = field(
        default=0,
        metadata={
            "name": "antennaPatternLength",
            "type": "Attribute",
        }
    )
    antenna_pattern_type: int = field(
        default=0,
        metadata={
            "name": "antennaPatternType",
            "type": "Attribute",
        }
    )
    crypto_key_id: int = field(
        default=0,
        metadata={
            "name": "cryptoKeyID",
            "type": "Attribute",
        }
    )
    crypto_system: int = field(
        default=0,
        metadata={
            "name": "cryptoSystem",
            "type": "Attribute",
        }
    )
    frequency: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    input_source: int = field(
        default=0,
        metadata={
            "name": "inputSource",
            "type": "Attribute",
        }
    )
    length_of_modulation_parameters: int = field(
        default=0,
        metadata={
            "name": "lengthOfModulationParameters",
            "type": "Attribute",
        }
    )
    modulation_type_detail: int = field(
        default=0,
        metadata={
            "name": "modulationTypeDetail",
            "type": "Attribute",
        }
    )
    modulation_type_major: int = field(
        default=0,
        metadata={
            "name": "modulationTypeMajor",
            "type": "Attribute",
        }
    )
    modulation_type_spread_spectrum: int = field(
        default=0,
        metadata={
            "name": "modulationTypeSpreadSpectrum",
            "type": "Attribute",
        }
    )
    modulation_type_system: int = field(
        default=0,
        metadata={
            "name": "modulationTypeSystem",
            "type": "Attribute",
        }
    )
    power: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    radio_entity_type_category: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeCategory",
            "type": "Attribute",
        }
    )
    radio_entity_type_country: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeCountry",
            "type": "Attribute",
        }
    )
    radio_entity_type_domain: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeDomain",
            "type": "Attribute",
        }
    )
    radio_entity_type_kind: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeKind",
            "type": "Attribute",
        }
    )
    radio_entity_type_nomenclature: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeNomenclature",
            "type": "Attribute",
        }
    )
    radio_entity_type_nomenclature_version: int = field(
        default=0,
        metadata={
            "name": "radioEntityTypeNomenclatureVersion",
            "type": "Attribute",
        }
    )
    relative_antenna_location: str = field(
        default="0 0 0",
        metadata={
            "name": "relativeAntennaLocation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    transmit_frequency_bandwidth: float = field(
        default=0.0,
        metadata={
            "name": "transmitFrequencyBandwidth",
            "type": "Attribute",
        }
    )
    transmit_state: int = field(
        default=0,
        metadata={
            "name": "transmitState",
            "type": "Attribute",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    geo_coords: str = field(
        default="0 0 0",
        metadata={
            "name": "geoCoords",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Viewpoint(X3DviewpointNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center_of_rotation: str = field(
        default="0 0 0",
        metadata={
            "name": "centerOfRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    field_of_view: float = field(
        default=0.7854,
        metadata={
            "name": "fieldOfView",
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_exclusive": 3.1416,
        }
    )
    position: str = field(
        default="0 0 10",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Viewport(X3DviewportNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    clip_boundary: str = field(
        default="0 1 0 1",
        metadata={
            "name": "clipBoundary",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="viewport",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class VisibilitySensor(X3DenvironmentalSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    center: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class VolumePickSensor(X3DpickSensorNode):
    """
    :ivar box:
    :ivar cone:
    :ivar cylinder:
    :ivar indexed_face_set:
    :ivar indexed_line_set:
    :ivar indexed_triangle_fan_set:
    :ivar indexed_triangle_set:
    :ivar indexed_triangle_strip_set:
    :ivar line_set:
    :ivar point_set:
    :ivar sphere:
    :ivar triangle_fan_set:
    :ivar triangle_set:
    :ivar triangle_strip_set:
    :ivar elevation_grid:
    :ivar polyline2_d:
    :ivar polypoint2_d:
    :ivar rectangle2_d:
    :ivar triangle_set2_d:
    :ivar extrusion:
    :ivar text:
    :ivar arc2_d:
    :ivar arc_close2_d:
    :ivar circle2_d:
    :ivar disk2_d:
    :ivar quad_set:
    :ivar indexed_quad_set:
    :ivar geo_elevation_grid:
    :ivar nurbs_curve:
    :ivar nurbs_patch_surface:
    :ivar nurbs_swept_surface:
    :ivar nurbs_swung_surface:
    :ivar nurbs_trimmed_surface:
    :ivar anchor:
    :ivar billboard:
    :ivar collision:
    :ivar group:
    :ivar inline:
    :ivar lod:
    :ivar static_group:
    :ivar switch:
    :ivar transform:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_transform:
    :ivar hanim_joint:
    :ivar nurbs_set:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar viewport:
    :ivar layout_group:
    :ivar screen_group:
    :ivar shape:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar container_field:
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    box: Optional["Box"] = field(
        default=None,
        metadata={
            "name": "Box",
            "type": "Element",
        }
    )
    cone: Optional["Cone"] = field(
        default=None,
        metadata={
            "name": "Cone",
            "type": "Element",
        }
    )
    cylinder: Optional["Cylinder"] = field(
        default=None,
        metadata={
            "name": "Cylinder",
            "type": "Element",
        }
    )
    indexed_face_set: Optional["IndexedFaceSet"] = field(
        default=None,
        metadata={
            "name": "IndexedFaceSet",
            "type": "Element",
        }
    )
    indexed_line_set: Optional["IndexedLineSet"] = field(
        default=None,
        metadata={
            "name": "IndexedLineSet",
            "type": "Element",
        }
    )
    indexed_triangle_fan_set: Optional["IndexedTriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleFanSet",
            "type": "Element",
        }
    )
    indexed_triangle_set: Optional["IndexedTriangleSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleSet",
            "type": "Element",
        }
    )
    indexed_triangle_strip_set: Optional["IndexedTriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "IndexedTriangleStripSet",
            "type": "Element",
        }
    )
    line_set: Optional["LineSet"] = field(
        default=None,
        metadata={
            "name": "LineSet",
            "type": "Element",
        }
    )
    point_set: Optional["PointSet"] = field(
        default=None,
        metadata={
            "name": "PointSet",
            "type": "Element",
        }
    )
    sphere: Optional["Sphere"] = field(
        default=None,
        metadata={
            "name": "Sphere",
            "type": "Element",
        }
    )
    triangle_fan_set: Optional["TriangleFanSet"] = field(
        default=None,
        metadata={
            "name": "TriangleFanSet",
            "type": "Element",
        }
    )
    triangle_set: Optional["TriangleSet"] = field(
        default=None,
        metadata={
            "name": "TriangleSet",
            "type": "Element",
        }
    )
    triangle_strip_set: Optional["TriangleStripSet"] = field(
        default=None,
        metadata={
            "name": "TriangleStripSet",
            "type": "Element",
        }
    )
    elevation_grid: Optional["ElevationGrid"] = field(
        default=None,
        metadata={
            "name": "ElevationGrid",
            "type": "Element",
        }
    )
    polyline2_d: Optional["Polyline2D"] = field(
        default=None,
        metadata={
            "name": "Polyline2D",
            "type": "Element",
        }
    )
    polypoint2_d: Optional["Polypoint2D"] = field(
        default=None,
        metadata={
            "name": "Polypoint2D",
            "type": "Element",
        }
    )
    rectangle2_d: Optional["Rectangle2D"] = field(
        default=None,
        metadata={
            "name": "Rectangle2D",
            "type": "Element",
        }
    )
    triangle_set2_d: Optional["TriangleSet2D"] = field(
        default=None,
        metadata={
            "name": "TriangleSet2D",
            "type": "Element",
        }
    )
    extrusion: Optional["Extrusion"] = field(
        default=None,
        metadata={
            "name": "Extrusion",
            "type": "Element",
        }
    )
    text: Optional["Text"] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    arc2_d: Optional["Arc2D"] = field(
        default=None,
        metadata={
            "name": "Arc2D",
            "type": "Element",
        }
    )
    arc_close2_d: Optional["ArcClose2D"] = field(
        default=None,
        metadata={
            "name": "ArcClose2D",
            "type": "Element",
        }
    )
    circle2_d: Optional["Circle2D"] = field(
        default=None,
        metadata={
            "name": "Circle2D",
            "type": "Element",
        }
    )
    disk2_d: Optional["Disk2D"] = field(
        default=None,
        metadata={
            "name": "Disk2D",
            "type": "Element",
        }
    )
    quad_set: Optional["QuadSet"] = field(
        default=None,
        metadata={
            "name": "QuadSet",
            "type": "Element",
        }
    )
    indexed_quad_set: Optional["IndexedQuadSet"] = field(
        default=None,
        metadata={
            "name": "IndexedQuadSet",
            "type": "Element",
        }
    )
    geo_elevation_grid: Optional["GeoElevationGrid"] = field(
        default=None,
        metadata={
            "name": "GeoElevationGrid",
            "type": "Element",
        }
    )
    nurbs_curve: Optional["NurbsCurve"] = field(
        default=None,
        metadata={
            "name": "NurbsCurve",
            "type": "Element",
        }
    )
    nurbs_patch_surface: Optional["NurbsPatchSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsPatchSurface",
            "type": "Element",
        }
    )
    nurbs_swept_surface: Optional["NurbsSweptSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSweptSurface",
            "type": "Element",
        }
    )
    nurbs_swung_surface: Optional["NurbsSwungSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsSwungSurface",
            "type": "Element",
        }
    )
    nurbs_trimmed_surface: Optional["NurbsTrimmedSurface"] = field(
        default=None,
        metadata={
            "name": "NurbsTrimmedSurface",
            "type": "Element",
        }
    )
    anchor: List["Anchor"] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "sequential": True,
        }
    )
    billboard: List["Billboard"] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
            "sequential": True,
        }
    )
    collision: List["Collision"] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    inline: List["Inline"] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
            "sequential": True,
        }
    )
    lod: List["Lod"] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
            "sequential": True,
        }
    )
    static_group: List["StaticGroup"] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    switch: List["Switch"] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
            "sequential": True,
        }
    )
    transform: List["Transform"] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "sequential": True,
        }
    )
    espdu_transform: List["EspduTransform"] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    receiver_pdu: List["ReceiverPdu"] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    signal_pdu: List["SignalPdu"] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    transmitter_pdu: List["TransmitterPdu"] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_location: List["GeoLocation"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_lod: List["GeoLod"] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
            "sequential": True,
        }
    )
    geo_transform: List["GeoTransform"] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
            "sequential": True,
        }
    )
    hanim_joint: List["HanimJoint"] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
            "sequential": True,
        }
    )
    nurbs_set: List["NurbsSet"] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
            "sequential": True,
        }
    )
    cadassembly: List["Cadassembly"] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
            "sequential": True,
        }
    )
    cadlayer: List["Cadlayer"] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
            "sequential": True,
        }
    )
    cadpart: List["Cadpart"] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
            "sequential": True,
        }
    )
    viewport: List["Viewport"] = field(
        default_factory=list,
        metadata={
            "name": "Viewport",
            "type": "Element",
            "sequential": True,
        }
    )
    layout_group: List["LayoutGroup"] = field(
        default_factory=list,
        metadata={
            "name": "LayoutGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    screen_group: List["ScreenGroup"] = field(
        default_factory=list,
        metadata={
            "name": "ScreenGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    shape: List["Shape"] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
            "sequential": True,
        }
    )
    proto_instance: List["ProtoInstance"] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
            "sequential": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class X3DdragSensorNode(X3DpointingDeviceSensorNode):
    class Meta:
        name = "X3DDragSensorNode"

    auto_offset: bool = field(
        default=True,
        metadata={
            "name": "autoOffset",
            "type": "Attribute",
        }
    )


@dataclass
class X3DtouchSensorNode(X3DpointingDeviceSensorNode):
    class Meta:
        name = "X3DTouchSensorNode"


@dataclass
class CylinderSensor(X3DdragSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    axis_rotation: str = field(
        default="0 1 0 0",
        metadata={
            "name": "axisRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    disk_angle: float = field(
        default=0.26179167,
        metadata={
            "name": "diskAngle",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.5708,
        }
    )
    max_angle: float = field(
        default=-1.0,
        metadata={
            "name": "maxAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    min_angle: float = field(
        default=0.0,
        metadata={
            "name": "minAngle",
            "type": "Attribute",
            "min_exclusive": -6.2832,
            "max_exclusive": 6.2832,
        }
    )
    offset: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class GeoTouchSensor(X3DtouchSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    geo_origin: Optional["GeoOrigin"] = field(
        default=None,
        metadata={
            "name": "GeoOrigin",
            "type": "Element",
        }
    )
    geo_system: List[str] = field(
        default_factory=lambda: [
            "\"GD\"",
            "\"WE\"",
        ],
        metadata={
            "name": "geoSystem",
            "type": "Attribute",
            "tokens": True,
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class PlaneSensor(X3DdragSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    axis_rotation: str = field(
        default="0 1 0 0",
        metadata={
            "name": "axisRotation",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    max_position: str = field(
        default="-1 -1",
        metadata={
            "name": "maxPosition",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    min_position: str = field(
        default="0 0",
        metadata={
            "name": "minPosition",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){1}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    offset: str = field(
        default="0 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class SphereSensor(X3DdragSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    offset: str = field(
        default="0 1 0 0",
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){3}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*",
        }
    )
    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class TouchSensor(X3DtouchSensorNode):
    class Meta:
        namespace = "http://www.design2machine.com"

    container_field: str = field(
        default="children",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )


@dataclass
class Scene(SceneGraphStructureStatement):
    """
    :ivar metadata_boolean:
    :ivar metadata_double:
    :ivar metadata_float:
    :ivar metadata_integer:
    :ivar metadata_set:
    :ivar metadata_string:
    :ivar background:
    :ivar color_interpolator:
    :ivar coordinate_interpolator:
    :ivar directional_light:
    :ivar group:
    :ivar navigation_info:
    :ivar normal_interpolator:
    :ivar orientation_interpolator:
    :ivar position_interpolator:
    :ivar scalar_interpolator:
    :ivar shape:
    :ivar time_sensor:
    :ivar transform:
    :ivar viewpoint:
    :ivar world_info:
    :ivar anchor:
    :ivar boolean_filter:
    :ivar boolean_sequencer:
    :ivar boolean_toggle:
    :ivar boolean_trigger:
    :ivar cylinder_sensor:
    :ivar inline:
    :ivar integer_sequencer:
    :ivar integer_trigger:
    :ivar key_sensor:
    :ivar plane_sensor:
    :ivar point_light:
    :ivar proximity_sensor:
    :ivar sphere_sensor:
    :ivar spot_light:
    :ivar string_sensor:
    :ivar switch:
    :ivar time_trigger:
    :ivar touch_sensor:
    :ivar audio_clip:
    :ivar billboard:
    :ivar collision:
    :ivar fog:
    :ivar load_sensor:
    :ivar local_fog:
    :ivar lod:
    :ivar script:
    :ivar sound:
    :ivar visibility_sensor:
    :ivar coordinate_interpolator2_d:
    :ivar position_interpolator2_d:
    :ivar clip_plane:
    :ivar ease_in_ease_out:
    :ivar line_pick_sensor:
    :ivar pickable_group:
    :ivar point_pick_sensor:
    :ivar primitive_pick_sensor:
    :ivar volume_pick_sensor:
    :ivar spline_position_interpolator:
    :ivar spline_position_interpolator2_d:
    :ivar spline_scalar_interpolator:
    :ivar squad_orientation_interpolator:
    :ivar static_group:
    :ivar cadassembly:
    :ivar cadlayer:
    :ivar cadpart:
    :ivar ortho_viewpoint:
    :ivar viewpoint_group:
    :ivar color_chaser:
    :ivar color_damper:
    :ivar coordinate_chaser:
    :ivar coordinate_damper:
    :ivar orientation_chaser:
    :ivar orientation_damper:
    :ivar position_chaser:
    :ivar position_chaser2_d:
    :ivar position_damper:
    :ivar position_damper2_d:
    :ivar scalar_chaser:
    :ivar scalar_damper:
    :ivar tex_coord_chaser2_d:
    :ivar tex_coord_damper2_d:
    :ivar texture_background:
    :ivar collidable_shape:
    :ivar collision_sensor:
    :ivar rigid_body_collection:
    :ivar particle_system:
    :ivar transform_sensor:
    :ivar iso_surface_volume_data:
    :ivar segmented_volume_data:
    :ivar volume_data:
    :ivar espdu_transform:
    :ivar receiver_pdu:
    :ivar signal_pdu:
    :ivar transmitter_pdu:
    :ivar disentity_manager:
    :ivar geo_location:
    :ivar geo_lod:
    :ivar geo_metadata:
    :ivar geo_position_interpolator:
    :ivar geo_proximity_sensor:
    :ivar geo_touch_sensor:
    :ivar geo_viewpoint:
    :ivar geo_transform:
    :ivar hanim_humanoid:
    :ivar hanim_joint:
    :ivar hanim_segment:
    :ivar hanim_site:
    :ivar nurbs_orientation_interpolator:
    :ivar nurbs_position_interpolator:
    :ivar nurbs_surface_interpolator:
    :ivar nurbs_set:
    :ivar proto_instance: Appropriately typed substitution node
    :ivar route:
    :ivar extern_proto_declare:
    :ivar proto_declare:
    :ivar import_value:
    :ivar export:
    :ivar layer_set: At most one LayerSet can appear in a scene and must
        be a root node.
    """
    class Meta:
        namespace = "http://www.design2machine.com"

    metadata_boolean: List[MetadataBoolean] = field(
        default_factory=list,
        metadata={
            "name": "MetadataBoolean",
            "type": "Element",
        }
    )
    metadata_double: List[MetadataDouble] = field(
        default_factory=list,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: List[MetadataFloat] = field(
        default_factory=list,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: List[MetadataInteger] = field(
        default_factory=list,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: List[MetadataSet] = field(
        default_factory=list,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: List[MetadataString] = field(
        default_factory=list,
        metadata={
            "name": "MetadataString",
            "type": "Element",
        }
    )
    background: List[Background] = field(
        default_factory=list,
        metadata={
            "name": "Background",
            "type": "Element",
        }
    )
    color_interpolator: List[ColorInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "ColorInterpolator",
            "type": "Element",
        }
    )
    coordinate_interpolator: List[CoordinateInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator",
            "type": "Element",
        }
    )
    directional_light: List[DirectionalLight] = field(
        default_factory=list,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        }
    )
    navigation_info: List[NavigationInfo] = field(
        default_factory=list,
        metadata={
            "name": "NavigationInfo",
            "type": "Element",
        }
    )
    normal_interpolator: List[NormalInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "NormalInterpolator",
            "type": "Element",
        }
    )
    orientation_interpolator: List[OrientationInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "OrientationInterpolator",
            "type": "Element",
        }
    )
    position_interpolator: List[PositionInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator",
            "type": "Element",
        }
    )
    scalar_interpolator: List[ScalarInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "ScalarInterpolator",
            "type": "Element",
        }
    )
    shape: List[Shape] = field(
        default_factory=list,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    time_sensor: List[TimeSensor] = field(
        default_factory=list,
        metadata={
            "name": "TimeSensor",
            "type": "Element",
        }
    )
    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        }
    )
    viewpoint: List[Viewpoint] = field(
        default_factory=list,
        metadata={
            "name": "Viewpoint",
            "type": "Element",
        }
    )
    world_info: List[WorldInfo] = field(
        default_factory=list,
        metadata={
            "name": "WorldInfo",
            "type": "Element",
        }
    )
    anchor: List[Anchor] = field(
        default_factory=list,
        metadata={
            "name": "Anchor",
            "type": "Element",
        }
    )
    boolean_filter: List[BooleanFilter] = field(
        default_factory=list,
        metadata={
            "name": "BooleanFilter",
            "type": "Element",
        }
    )
    boolean_sequencer: List[BooleanSequencer] = field(
        default_factory=list,
        metadata={
            "name": "BooleanSequencer",
            "type": "Element",
        }
    )
    boolean_toggle: List[BooleanToggle] = field(
        default_factory=list,
        metadata={
            "name": "BooleanToggle",
            "type": "Element",
        }
    )
    boolean_trigger: List[BooleanTrigger] = field(
        default_factory=list,
        metadata={
            "name": "BooleanTrigger",
            "type": "Element",
        }
    )
    cylinder_sensor: List[CylinderSensor] = field(
        default_factory=list,
        metadata={
            "name": "CylinderSensor",
            "type": "Element",
        }
    )
    inline: List[Inline] = field(
        default_factory=list,
        metadata={
            "name": "Inline",
            "type": "Element",
        }
    )
    integer_sequencer: List[IntegerSequencer] = field(
        default_factory=list,
        metadata={
            "name": "IntegerSequencer",
            "type": "Element",
        }
    )
    integer_trigger: List[IntegerTrigger] = field(
        default_factory=list,
        metadata={
            "name": "IntegerTrigger",
            "type": "Element",
        }
    )
    key_sensor: List[KeySensor] = field(
        default_factory=list,
        metadata={
            "name": "KeySensor",
            "type": "Element",
        }
    )
    plane_sensor: List[PlaneSensor] = field(
        default_factory=list,
        metadata={
            "name": "PlaneSensor",
            "type": "Element",
        }
    )
    point_light: List[PointLight] = field(
        default_factory=list,
        metadata={
            "name": "PointLight",
            "type": "Element",
        }
    )
    proximity_sensor: List[ProximitySensor] = field(
        default_factory=list,
        metadata={
            "name": "ProximitySensor",
            "type": "Element",
        }
    )
    sphere_sensor: List[SphereSensor] = field(
        default_factory=list,
        metadata={
            "name": "SphereSensor",
            "type": "Element",
        }
    )
    spot_light: List[SpotLight] = field(
        default_factory=list,
        metadata={
            "name": "SpotLight",
            "type": "Element",
        }
    )
    string_sensor: List[StringSensor] = field(
        default_factory=list,
        metadata={
            "name": "StringSensor",
            "type": "Element",
        }
    )
    switch: List[Switch] = field(
        default_factory=list,
        metadata={
            "name": "Switch",
            "type": "Element",
        }
    )
    time_trigger: List[TimeTrigger] = field(
        default_factory=list,
        metadata={
            "name": "TimeTrigger",
            "type": "Element",
        }
    )
    touch_sensor: List[TouchSensor] = field(
        default_factory=list,
        metadata={
            "name": "TouchSensor",
            "type": "Element",
        }
    )
    audio_clip: List[AudioClip] = field(
        default_factory=list,
        metadata={
            "name": "AudioClip",
            "type": "Element",
        }
    )
    billboard: List[Billboard] = field(
        default_factory=list,
        metadata={
            "name": "Billboard",
            "type": "Element",
        }
    )
    collision: List[Collision] = field(
        default_factory=list,
        metadata={
            "name": "Collision",
            "type": "Element",
        }
    )
    fog: List[Fog] = field(
        default_factory=list,
        metadata={
            "name": "Fog",
            "type": "Element",
        }
    )
    load_sensor: List[LoadSensor] = field(
        default_factory=list,
        metadata={
            "name": "LoadSensor",
            "type": "Element",
        }
    )
    local_fog: List[LocalFog] = field(
        default_factory=list,
        metadata={
            "name": "LocalFog",
            "type": "Element",
        }
    )
    lod: List[Lod] = field(
        default_factory=list,
        metadata={
            "name": "LOD",
            "type": "Element",
        }
    )
    script: List[Script] = field(
        default_factory=list,
        metadata={
            "name": "Script",
            "type": "Element",
        }
    )
    sound: List[Sound] = field(
        default_factory=list,
        metadata={
            "name": "Sound",
            "type": "Element",
        }
    )
    visibility_sensor: List[VisibilitySensor] = field(
        default_factory=list,
        metadata={
            "name": "VisibilitySensor",
            "type": "Element",
        }
    )
    coordinate_interpolator2_d: List[CoordinateInterpolator2D] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateInterpolator2D",
            "type": "Element",
        }
    )
    position_interpolator2_d: List[PositionInterpolator2D] = field(
        default_factory=list,
        metadata={
            "name": "PositionInterpolator2D",
            "type": "Element",
        }
    )
    clip_plane: List[ClipPlane] = field(
        default_factory=list,
        metadata={
            "name": "ClipPlane",
            "type": "Element",
        }
    )
    ease_in_ease_out: List[EaseInEaseOut] = field(
        default_factory=list,
        metadata={
            "name": "EaseInEaseOut",
            "type": "Element",
        }
    )
    line_pick_sensor: List[LinePickSensor] = field(
        default_factory=list,
        metadata={
            "name": "LinePickSensor",
            "type": "Element",
        }
    )
    pickable_group: List[PickableGroup] = field(
        default_factory=list,
        metadata={
            "name": "PickableGroup",
            "type": "Element",
        }
    )
    point_pick_sensor: List[PointPickSensor] = field(
        default_factory=list,
        metadata={
            "name": "PointPickSensor",
            "type": "Element",
        }
    )
    primitive_pick_sensor: List[PrimitivePickSensor] = field(
        default_factory=list,
        metadata={
            "name": "PrimitivePickSensor",
            "type": "Element",
        }
    )
    volume_pick_sensor: List[VolumePickSensor] = field(
        default_factory=list,
        metadata={
            "name": "VolumePickSensor",
            "type": "Element",
        }
    )
    spline_position_interpolator: List[SplinePositionInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator",
            "type": "Element",
        }
    )
    spline_position_interpolator2_d: List[SplinePositionInterpolator2D] = field(
        default_factory=list,
        metadata={
            "name": "SplinePositionInterpolator2D",
            "type": "Element",
        }
    )
    spline_scalar_interpolator: List[SplineScalarInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "SplineScalarInterpolator",
            "type": "Element",
        }
    )
    squad_orientation_interpolator: List[SquadOrientationInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "SquadOrientationInterpolator",
            "type": "Element",
        }
    )
    static_group: List[StaticGroup] = field(
        default_factory=list,
        metadata={
            "name": "StaticGroup",
            "type": "Element",
        }
    )
    cadassembly: List[Cadassembly] = field(
        default_factory=list,
        metadata={
            "name": "CADAssembly",
            "type": "Element",
        }
    )
    cadlayer: List[Cadlayer] = field(
        default_factory=list,
        metadata={
            "name": "CADLayer",
            "type": "Element",
        }
    )
    cadpart: List[Cadpart] = field(
        default_factory=list,
        metadata={
            "name": "CADPart",
            "type": "Element",
        }
    )
    ortho_viewpoint: List[OrthoViewpoint] = field(
        default_factory=list,
        metadata={
            "name": "OrthoViewpoint",
            "type": "Element",
        }
    )
    viewpoint_group: List[ViewpointGroup] = field(
        default_factory=list,
        metadata={
            "name": "ViewpointGroup",
            "type": "Element",
        }
    )
    color_chaser: List[ColorChaser] = field(
        default_factory=list,
        metadata={
            "name": "ColorChaser",
            "type": "Element",
        }
    )
    color_damper: List[ColorDamper] = field(
        default_factory=list,
        metadata={
            "name": "ColorDamper",
            "type": "Element",
        }
    )
    coordinate_chaser: List[CoordinateChaser] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateChaser",
            "type": "Element",
        }
    )
    coordinate_damper: List[CoordinateDamper] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateDamper",
            "type": "Element",
        }
    )
    orientation_chaser: List[OrientationChaser] = field(
        default_factory=list,
        metadata={
            "name": "OrientationChaser",
            "type": "Element",
        }
    )
    orientation_damper: List[OrientationDamper] = field(
        default_factory=list,
        metadata={
            "name": "OrientationDamper",
            "type": "Element",
        }
    )
    position_chaser: List[PositionChaser] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser",
            "type": "Element",
        }
    )
    position_chaser2_d: List[PositionChaser2D] = field(
        default_factory=list,
        metadata={
            "name": "PositionChaser2D",
            "type": "Element",
        }
    )
    position_damper: List[PositionDamper] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper",
            "type": "Element",
        }
    )
    position_damper2_d: List[PositionDamper2D] = field(
        default_factory=list,
        metadata={
            "name": "PositionDamper2D",
            "type": "Element",
        }
    )
    scalar_chaser: List[ScalarChaser] = field(
        default_factory=list,
        metadata={
            "name": "ScalarChaser",
            "type": "Element",
        }
    )
    scalar_damper: List[ScalarDamper] = field(
        default_factory=list,
        metadata={
            "name": "ScalarDamper",
            "type": "Element",
        }
    )
    tex_coord_chaser2_d: List[TexCoordChaser2D] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordChaser2D",
            "type": "Element",
        }
    )
    tex_coord_damper2_d: List[TexCoordDamper2D] = field(
        default_factory=list,
        metadata={
            "name": "TexCoordDamper2D",
            "type": "Element",
        }
    )
    texture_background: List[TextureBackground] = field(
        default_factory=list,
        metadata={
            "name": "TextureBackground",
            "type": "Element",
        }
    )
    collidable_shape: List[CollidableShape] = field(
        default_factory=list,
        metadata={
            "name": "CollidableShape",
            "type": "Element",
        }
    )
    collision_sensor: List[CollisionSensor] = field(
        default_factory=list,
        metadata={
            "name": "CollisionSensor",
            "type": "Element",
        }
    )
    rigid_body_collection: List[RigidBodyCollection] = field(
        default_factory=list,
        metadata={
            "name": "RigidBodyCollection",
            "type": "Element",
        }
    )
    particle_system: List[ParticleSystem] = field(
        default_factory=list,
        metadata={
            "name": "ParticleSystem",
            "type": "Element",
        }
    )
    transform_sensor: List[TransformSensor] = field(
        default_factory=list,
        metadata={
            "name": "TransformSensor",
            "type": "Element",
        }
    )
    iso_surface_volume_data: List[IsoSurfaceVolumeData] = field(
        default_factory=list,
        metadata={
            "name": "IsoSurfaceVolumeData",
            "type": "Element",
        }
    )
    segmented_volume_data: List[SegmentedVolumeData] = field(
        default_factory=list,
        metadata={
            "name": "SegmentedVolumeData",
            "type": "Element",
        }
    )
    volume_data: List[VolumeData] = field(
        default_factory=list,
        metadata={
            "name": "VolumeData",
            "type": "Element",
        }
    )
    espdu_transform: List[EspduTransform] = field(
        default_factory=list,
        metadata={
            "name": "EspduTransform",
            "type": "Element",
        }
    )
    receiver_pdu: List[ReceiverPdu] = field(
        default_factory=list,
        metadata={
            "name": "ReceiverPdu",
            "type": "Element",
        }
    )
    signal_pdu: List[SignalPdu] = field(
        default_factory=list,
        metadata={
            "name": "SignalPdu",
            "type": "Element",
        }
    )
    transmitter_pdu: List[TransmitterPdu] = field(
        default_factory=list,
        metadata={
            "name": "TransmitterPdu",
            "type": "Element",
        }
    )
    disentity_manager: List[DisentityManager] = field(
        default_factory=list,
        metadata={
            "name": "DISEntityManager",
            "type": "Element",
        }
    )
    geo_location: List[GeoLocation] = field(
        default_factory=list,
        metadata={
            "name": "GeoLocation",
            "type": "Element",
        }
    )
    geo_lod: List[GeoLod] = field(
        default_factory=list,
        metadata={
            "name": "GeoLOD",
            "type": "Element",
        }
    )
    geo_metadata: List[GeoMetadata] = field(
        default_factory=list,
        metadata={
            "name": "GeoMetadata",
            "type": "Element",
        }
    )
    geo_position_interpolator: List[GeoPositionInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "GeoPositionInterpolator",
            "type": "Element",
        }
    )
    geo_proximity_sensor: List[GeoProximitySensor] = field(
        default_factory=list,
        metadata={
            "name": "GeoProximitySensor",
            "type": "Element",
        }
    )
    geo_touch_sensor: List[GeoTouchSensor] = field(
        default_factory=list,
        metadata={
            "name": "GeoTouchSensor",
            "type": "Element",
        }
    )
    geo_viewpoint: List[GeoViewpoint] = field(
        default_factory=list,
        metadata={
            "name": "GeoViewpoint",
            "type": "Element",
        }
    )
    geo_transform: List[GeoTransform] = field(
        default_factory=list,
        metadata={
            "name": "GeoTransform",
            "type": "Element",
        }
    )
    hanim_humanoid: List[HanimHumanoid] = field(
        default_factory=list,
        metadata={
            "name": "HAnimHumanoid",
            "type": "Element",
        }
    )
    hanim_joint: List[HanimJoint] = field(
        default_factory=list,
        metadata={
            "name": "HAnimJoint",
            "type": "Element",
        }
    )
    hanim_segment: List[HanimSegment] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSegment",
            "type": "Element",
        }
    )
    hanim_site: List[HanimSite] = field(
        default_factory=list,
        metadata={
            "name": "HAnimSite",
            "type": "Element",
        }
    )
    nurbs_orientation_interpolator: List[NurbsOrientationInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "NurbsOrientationInterpolator",
            "type": "Element",
        }
    )
    nurbs_position_interpolator: List[NurbsPositionInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "NurbsPositionInterpolator",
            "type": "Element",
        }
    )
    nurbs_surface_interpolator: List[NurbsSurfaceInterpolator] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSurfaceInterpolator",
            "type": "Element",
        }
    )
    nurbs_set: List[NurbsSet] = field(
        default_factory=list,
        metadata={
            "name": "NurbsSet",
            "type": "Element",
        }
    )
    proto_instance: List[ProtoInstance] = field(
        default_factory=list,
        metadata={
            "name": "ProtoInstance",
            "type": "Element",
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "ROUTE",
            "type": "Element",
        }
    )
    extern_proto_declare: List[ExternProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ExternProtoDeclare",
            "type": "Element",
        }
    )
    proto_declare: List[ProtoDeclare] = field(
        default_factory=list,
        metadata={
            "name": "ProtoDeclare",
            "type": "Element",
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "IMPORT",
            "type": "Element",
        }
    )
    export: List[Export] = field(
        default_factory=list,
        metadata={
            "name": "EXPORT",
            "type": "Element",
        }
    )
    layer_set: List[LayerSet] = field(
        default_factory=list,
        metadata={
            "name": "LayerSet",
            "type": "Element",
        }
    )


@dataclass
class X3D(SceneGraphStructureStatement):
    class Meta:
        namespace = "http://www.design2machine.com"

    head: Optional[Head] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    scene: Optional[Scene] = field(
        default=None,
        metadata={
            "name": "Scene",
            "type": "Element",
            "required": True,
        }
    )
    version: Optional[X3DVersionChoices] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    profile: Optional[ProfileNameChoices] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
