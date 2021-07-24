from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from btlx.x3d_3_3 import X3DshapeNode

__NAMESPACE__ = "http://www.design2machine.com"


class AlignmentHorizontalType(Enum):
    """
    Alignment of a text (left, center, right)
    """
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class AlignmentVerticalType(Enum):
    """
    Alignment of a text (bottom, center, top)
    """
    BOTTOM = "bottom"
    CENTER = "center"
    TOP = "top"


class ArcShapeType(Enum):
    """
    Shape of a profile arc (convex, concave)
    """
    CONVEX = "convex"
    CONCAVE = "concave"


class BtlxVersion(Enum):
    VALUE_1_1 = "1.1"


class BooleanType(Enum):
    """
    (yes, no)
    """
    YES = "yes"
    NO = "no"


@dataclass
class CamberType:
    """
    Defintion of a camber.
    """
    reference_plane_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencePlaneID",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )
    starting_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartingPoint",
            "type": "Attribute",
            "required": True,
        }
    )
    end_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Attribute",
            "required": True,
        }
    )
    camber_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "CamberPoint",
            "type": "Attribute",
            "required": True,
        }
    )
    camber: Optional[float] = field(
        default=None,
        metadata={
            "name": "Camber",
            "type": "Attribute",
            "required": True,
        }
    )


class ChamferExitType(Enum):
    """
    Shape the chamfer exit (orthogonal, angular, round)
    """
    ORTHOGONAL = "orthogonal"
    ANGULAR = "angular"
    ROUND = "round"


@dataclass
class ColourType:
    """
    Definition of a colour (red, green, blue, transparency)
    """
    red: Optional[int] = field(
        default=None,
        metadata={
            "name": "Red",
            "type": "Attribute",
            "required": True,
        }
    )
    green: Optional[int] = field(
        default=None,
        metadata={
            "name": "Green",
            "type": "Attribute",
            "required": True,
        }
    )
    blue: Optional[int] = field(
        default=None,
        metadata={
            "name": "Blue",
            "type": "Attribute",
            "required": True,
        }
    )
    transparency: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transparency",
            "type": "Attribute",
            "required": True,
        }
    )


class ContourRecessType(Enum):
    """
    Type of recess for the contour (automatic, noPassOver, passOverStart,
    passOverEnd, passOverAll)
    """
    AUTOMATIC = "automatic"
    NO_PASS_OVER = "noPassOver"
    PASS_OVER_START = "passOverStart"
    PASS_OVER_END = "passOverEnd"
    PASS_OVER_ALL = "passOverAll"


class ContourType(Enum):
    """
    Type of the contour (freeContour, sawContour, ...) not used.
    """
    FREE_CONTOUR = "freeContour"
    SAW_CONTOUR = "sawContour"
    MILL_CONTOUR = "millContour"
    PEN_CONTOUR = "penContour"
    NAIL_CONTOUR = "nailContour"
    GLUE_AREA = "glueArea"
    PLANNING_AREA = "planningArea"
    PLASTER_AREA = "plasterArea"
    LOCKOUT_AREA = "lockoutArea"


@dataclass
class CoordinateType:
    """
    Definition of a vector or point.
    """
    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        }
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Attribute",
            "required": True,
        }
    )


class DovetailShapeType(Enum):
    """
    Shape of the dovetail (european, american)
    """
    EUROPEAN = "european"
    AMERICAN = "american"


class EdgePositionType(Enum):
    """
    Position on the reference side (refedge, oppedge)
    """
    REFEDGE = "refedge"
    OPPEDGE = "oppedge"


class EndType(Enum):
    """
    Type of the separating cut (rectangular, angled, double)
    """
    RECTANGULAR_CUT = "rectangularCut"
    ANGLED_CUT = "angledCut"
    DOUBLE_CUT = "doubleCut"


class LapExitType(Enum):
    """
    Shape the lap exit (none, mitre, rebate)
    """
    NONE = "none"
    MITRE = "mitre"
    REBATE = "rebate"


class LimitationTopType(Enum):
    """
    Limitation of a dovetail mortise at the top (limited, unlimited, pocket)
    """
    LIMITED = "limited"
    UNLIMITED = "unlimited"
    POCKET = "pocket"


class LocationType(Enum):
    """
    Type of the location of a wall beam (top/bottom rail, horizontal, vertical,
    angled element)
    """
    BOTTOM_RAIL = "bottomRail"
    TOP_RAIL = "topRail"
    BOTTOM_RAIL_ANGLED = "bottomRailAngled"
    TOP_RAIL_ANGLED = "topRailAngled"
    HORIZONTAL_COMPONENT = "horizontalComponent"
    VERTICAL_COMPONENT = "verticalComponent"
    ANGLED_COMPONENT = "angledComponent"


class LogLapPositionType(Enum):
    """
    Position of the laps (symmetric, forward, backward)
    """
    SYMMETRIC = "symmetric"
    FORWARD = "forward"
    BACKWARD = "backward"


class MarkingStyleType(Enum):
    """
    Style of a marking (single, double, square)
    """
    SINGLE = "single"
    DOUBLE = "double"
    SQUARE = "square"


class MaterialGroupType(Enum):
    """
    Type of the material (for wall construction)
    """
    BATTEN = "batten"
    CLADDING = "cladding"
    MASSIVE_TIMBER = "massiveTimber"
    MEMBRANE = "membrane"
    GYPSUM_BOARD = "gypsumBoard"
    GYPSUM_FIBRE = "gypsumFibre"
    INSULATION = "insulation"
    SHEET_COMPONENT = "sheetComponent"
    FACADE_PANEL = "facadePanel"
    PROFILED_PANEL = "profiledPanel"
    PLASTER = "plaster"


class OrientationType(Enum):
    """
    Orientation of a processing (start, end)
    """
    START = "start"
    END = "end"


@dataclass
class PartOffsetType:
    """
    Definition of a part offset.
    """
    flush_side: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlushSide",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 4,
        }
    )
    offset_side1: float = field(
        default=0.0,
        metadata={
            "name": "OffsetSide1",
            "type": "Attribute",
        }
    )
    offset_side2: float = field(
        default=0.0,
        metadata={
            "name": "OffsetSide2",
            "type": "Attribute",
        }
    )
    offset_side3: float = field(
        default=0.0,
        metadata={
            "name": "OffsetSide3",
            "type": "Attribute",
        }
    )
    offset_side4: float = field(
        default=0.0,
        metadata={
            "name": "OffsetSide4",
            "type": "Attribute",
        }
    )


class PremillType(Enum):
    """
    Shape the profile cambered premill (round, angular)
    """
    ROUND = "round"
    ANGULAR = "angular"


class ProcessSideType(Enum):
    """
    Sides for the processing (both, refside, oppside)
    """
    BOTH = "both"
    REFSIDE = "refside"
    OPPSIDE = "oppside"


class ProcessingQualityType(Enum):
    """
    Quality of a processing (automatic, visible, fast)
    """
    AUTOMATIC = "automatic"
    VISIBLE = "visible"
    FAST = "fast"


@dataclass
class ProgramInfoType:
    """
    Information about the program that exports/modifies the data.

    :ivar company_name:
    :ivar program_name:
    :ivar program_version:
    :ivar computer_name:
    :ivar user_name:
    :ivar file_name:
    :ivar date: in compliance with ISO 8601
    :ivar time:
    :ivar comment:
    """
    company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
        }
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
        }
    )
    program_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramVersion",
            "type": "Attribute",
        }
    )
    computer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComputerName",
            "type": "Attribute",
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Attribute",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        }
    )
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        }
    )


class RecessType(Enum):
    """
    Recess of a processing (automatic, manual)
    """
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class ScarfShapeType(Enum):
    """
    Shape of a scarf (refside, baseside, classic)
    """
    REFSIDE = "refside"
    BASESIDE = "baseside"
    CLASSIC = "classic"


class StepShapeType(Enum):
    """
    Shape of a step joint (double, step, heel, taperedheel)
    """
    DOUBLE = "double"
    STEP = "step"
    HEEL = "heel"
    TAPEREDHEEL = "taperedheel"


class StoreyType(Enum):
    """
    Type of the storey (none, ceiling, roof, wall)
    """
    VALUE = ""
    CEILING = "ceiling"
    ROOF = "roof"
    WALL = "wall"


class TenonShapeType(Enum):
    """
    Shape of a tenon, mortise or house (automatic, square, round, rounded,
    radius)
    """
    AUTOMATIC = "automatic"
    SQUARE = "square"
    ROUND = "round"
    ROUNDED = "rounded"
    RADIUS = "radius"


class ToolPositionType(Enum):
    """
    Position of the tool (left, center, right)
    """
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class TyroleanDovetailShapeType(Enum):
    """
    Shape of the tyrolean dovetail (angular, straight)
    """
    ANGULAR = "angular"
    STRAIGHT = "straight"


@dataclass
class UserAttributeType:
    """
    Definition of a user-defined attribute.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VariantParameterType:
    """
    Definition of a parameter in a variant.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    string_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "StringValue",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlignmentType:
    """
    Definition of an alignment in a wall.
    """
    location: Optional[LocationType] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "required": True,
        }
    )
    endtype: Optional[EndType] = field(
        default=None,
        metadata={
            "name": "Endtype",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoordinateSystemType:
    """
    Definition of a local coordinate system.
    """
    reference_point: Optional[CoordinateType] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    xvector: Optional[CoordinateType] = field(
        default=None,
        metadata={
            "name": "XVector",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    yvector: Optional[CoordinateType] = field(
        default=None,
        metadata={
            "name": "YVector",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )


@dataclass
class LineType:
    """
    Definition of a contour line.
    """
    end_point: Optional[CoordinateType] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Attribute",
            "min_inclusive": -89.9,
            "max_inclusive": 89.9,
        }
    )
    nail_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "NailSpacing",
            "type": "Attribute",
        }
    )
    recess: Optional[ContourRecessType] = field(
        default=None,
        metadata={
            "name": "Recess",
            "type": "Attribute",
        }
    )
    process: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Process",
            "type": "Attribute",
        }
    )


@dataclass
class MachiningLimitType:
    """
    Definition of the limited faces of a processing.
    """
    face_limited_start: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "FaceLimitedStart",
            "type": "Attribute",
        }
    )
    face_limited_end: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "FaceLimitedEnd",
            "type": "Attribute",
        }
    )
    face_limited_front: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "FaceLimitedFront",
            "type": "Attribute",
        }
    )
    face_limited_back: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "FaceLimitedBack",
            "type": "Attribute",
        }
    )
    face_limited_top: BooleanType = field(
        default=BooleanType.NO,
        metadata={
            "name": "FaceLimitedTop",
            "type": "Attribute",
        }
    )
    face_limited_bottom: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "FaceLimitedBottom",
            "type": "Attribute",
        }
    )


@dataclass
class MaterialClassType:
    """
    Definition of a material.
    """
    group: Optional[MaterialGroupType] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "required": True,
        }
    )
    specification: Optional[str] = field(
        default=None,
        metadata={
            "name": "Specification",
            "type": "Attribute",
        }
    )


@dataclass
class PointType(CoordinateType):
    """
    Defintion of a contour point.
    """


@dataclass
class ProcessingBaseType:
    """
    Definition of a machining to be executed on the superior part.
    """
    user_attributes: Optional["ProcessingBaseType.UserAttributes"] = field(
        default=None,
        metadata={
            "name": "UserAttributes",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    process: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "Process",
            "type": "Attribute",
        }
    )
    processing_quality: Optional[ProcessingQualityType] = field(
        default=None,
        metadata={
            "name": "ProcessingQuality",
            "type": "Attribute",
        }
    )
    recess: Optional[RecessType] = field(
        default=None,
        metadata={
            "name": "Recess",
            "type": "Attribute",
        }
    )
    priority: int = field(
        default=0,
        metadata={
            "name": "Priority",
            "type": "Attribute",
        }
    )
    process_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProcessID",
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        }
    )

    @dataclass
    class UserAttributes:
        user_attribute: List[UserAttributeType] = field(
            default_factory=list,
            metadata={
                "name": "UserAttribute",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class ProfileArcType:
    """
    Defintion of a profile arc.
    """
    quarter_arc: Optional["ProfileArcType.QuarterArc"] = field(
        default=None,
        metadata={
            "name": "QuarterArc",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    segment: Optional["ProfileArcType.Segment"] = field(
        default=None,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_shape: ArcShapeType = field(
        default=ArcShapeType.CONVEX,
        metadata={
            "name": "ArcShape",
            "type": "Attribute",
        }
    )
    lap_length: float = field(
        default=10.0,
        metadata={
            "name": "LapLength",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    lap_height: float = field(
        default=10.0,
        metadata={
            "name": "LapHeight",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    displacement: float = field(
        default=10.0,
        metadata={
            "name": "Displacement",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )

    @dataclass
    class QuarterArc:
        radius: float = field(
            default=50.0,
            metadata={
                "name": "Radius",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 1000.0,
            }
        )

    @dataclass
    class Segment:
        length: float = field(
            default=50.0,
            metadata={
                "name": "Length",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 1000.0,
            }
        )
        height: float = field(
            default=50.0,
            metadata={
                "name": "Height",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 1000.0,
            }
        )
        camber: float = field(
            default=50.0,
            metadata={
                "name": "Camber",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 1000.0,
            }
        )


@dataclass
class ShapeType(X3DshapeNode):
    """
    Definition of a X3D shape.
    """


@dataclass
class ArcType(LineType):
    """
    Definition of a contour arc.
    """
    point_on_arc: Optional[CoordinateType] = field(
        default=None,
        metadata={
            "name": "PointOnArc",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )


@dataclass
class ChamferType(ProcessingBaseType):
    """
    Definition of a chamfer.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "StartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    end_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "EndLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    chamfer_edge12: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ChamferEdge12",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    chamfer_edge23: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ChamferEdge23",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    chamfer_edge34: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ChamferEdge34",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    chamfer_edge41: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ChamferEdge41",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    chamfer_exit: Optional[ChamferExitType] = field(
        default=None,
        metadata={
            "name": "ChamferExit",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class PlaningType(ProcessingBaseType):
    """
    Definition of a planing.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    start_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "StartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    end_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "EndLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    plane_side1: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "PlaneSide1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    plane_side2: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "PlaneSide2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    plane_side3: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "PlaneSide3",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    plane_side4: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "PlaneSide4",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class ProcessingType(ProcessingBaseType):
    """
    Definition of a machining to be executed on the superior part.

    :ivar reference_plane_id: can refer to a global reference plane
        (1-6) or a user defined reference plane (100-)
    """
    reference_plane_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencePlaneID",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        }
    )


@dataclass
class ReferenceType:
    """
    defines the placement of a component in a superior component or of a
    ProcessingType in a part.
    """
    position: Optional[CoordinateSystemType] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUID",
            "type": "Attribute",
            "required": True,
            "pattern": r"\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}",
        }
    )


@dataclass
class UserReferencePlaneType:
    """
    Definition of a user reference plane (in relation to the part coordinate
    system)
    """
    position: Optional[CoordinateSystemType] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 100,
        }
    )


@dataclass
class BirdsMouthType(ProcessingType):
    """
    Definition of a birds mouth.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 180.0,
        }
    )
    inclination2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 180.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width_counter_part_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "WidthCounterPartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    width_counter_part: Optional[float] = field(
        default=None,
        metadata={
            "name": "WidthCounterPart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    height_counter_part_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "HeightCounterPartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    height_counter_part: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightCounterPart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    face_limited_front: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "FaceLimitedFront",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    face_limited_back: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "FaceLimitedBack",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lead_angle_parallel: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LeadAngleParallel",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lead_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "LeadAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    lead_inclination_parallel: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LeadInclinationParallel",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lead_inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "LeadInclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    rafter_nail_hole: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "RafterNailHole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class DoubleCutType(ProcessingType):
    """
    Defintion of a double cut.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )


@dataclass
class DovetailMortiseType(ProcessingType):
    """
    Definition of a dovetail mortise.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    limitation_top: Optional[LimitationTopType] = field(
        default=None,
        metadata={
            "name": "LimitationTop",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length_limited_bottom: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedBottom",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    cone_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "ConeAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 30.0,
        }
    )
    use_flank_angle: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "UseFlankAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    flank_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "FlankAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 5.0,
            "max_inclusive": 35.0,
        }
    )
    shape: Optional[TenonShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShapeRadius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class DovetailTenonType(ProcessingType):
    """
    Definition of a dovetail tenon.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    rotation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length_limited_top: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedTop",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length_limited_bottom: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedBottom",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    cone_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "ConeAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 30.0,
        }
    )
    use_flank_angle: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "UseFlankAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    flank_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "FlankAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 5.0,
            "max_inclusive": 35.0,
        }
    )
    shape: Optional[TenonShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShapeRadius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class DovetailType(ProcessingType):
    """
    Definition of a dovetail.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    cut_off: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "CutOff",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 45.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    rebate_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "RebateLength",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    height_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    height_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    lap_position: Optional[EdgePositionType] = field(
        default=None,
        metadata={
            "name": "LapPosition",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lap_exit: Optional[LapExitType] = field(
        default=None,
        metadata={
            "name": "LapExit",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape: Optional[DovetailShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    process_side: Optional[ProcessSideType] = field(
        default=None,
        metadata={
            "name": "ProcessSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class DrillingType(ProcessingType):
    """
    Definition of a drilling.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 360.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    depth_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "DepthLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    diameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )


@dataclass
class FrenchRidgeLapType(ProcessingType):
    """
    Definition of a french ridge lap.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    ref_position: Optional[EdgePositionType] = field(
        default=None,
        metadata={
            "name": "RefPosition",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    drillhole: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Drillhole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    drillhole_diam: Optional[float] = field(
        default=None,
        metadata={
            "name": "DrillholeDiam",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class HipValleyRafterNotchType(ProcessingType):
    """
    Definition of a hip or valley rafter notch.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle_ref_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleRefEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_opp_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleOppEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 180.0,
        }
    )
    width_counter_part_ref_edge_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "WidthCounterPartRefEdgeLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    width_counter_part_ref_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "WidthCounterPartRefEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width_counter_part_opp_edge_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "WidthCounterPartOppEdgeLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    width_counter_part_opp_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "WidthCounterPartOppEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    rafter_nail_hole: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "RafterNailHole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class JackRafterCutType(ProcessingType):
    """
    Defintion of a jackrafter cut.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )


@dataclass
class LapType(ProcessingType):
    """
    Definition of a lap.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -89.9,
            "max_inclusive": 89.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    lead_angle_parallel: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LeadAngleParallel",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lead_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "LeadAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    lead_inclination_parallel: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LeadInclinationParallel",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lead_inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "LeadInclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    machining_limits: Optional[MachiningLimitType] = field(
        default=None,
        metadata={
            "name": "MachiningLimits",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class LogHouseFrontType(ProcessingType):
    """
    Definition of a log house front joint.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_ref_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthRefEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    ref_side_only: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "RefSideOnly",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class LogHouseHalfLapType(ProcessingType):
    """
    Definition of a log house half lap.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )


@dataclass
class LogHouseJointType(ProcessingType):
    """
    Definition of a log house joint.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    side_laps_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "SideLapsLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    depth_side_laps: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthSideLaps",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    lap_position: Optional[LogLapPositionType] = field(
        default=None,
        metadata={
            "name": "LapPosition",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "LengthRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    length_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "LengthOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    length_ref_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "LengthRefEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_ref_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthRefEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    length_opp_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "LengthOppEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_edge: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppEdge",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    drillhole: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Drillhole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_ref_edge_start: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ArcRefEdgeStart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_ref_edge_end: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ArcRefEdgeEnd",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_opp_edge_start: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ArcOppEdgeStart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_opp_edge_end: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "ArcOppEdgeEnd",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    arc_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "ArcRadius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    arc_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "ArcDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    arc_center: Optional[float] = field(
        default=None,
        metadata={
            "name": "ArcCenter",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )


@dataclass
class LongitudinalCutType(ProcessingType):
    """
    Definition of a longitudinal cut.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )
    start_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "StartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    end_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "EndLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    depth_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "DepthLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleStart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleEnd",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    tool_position: Optional[ToolPositionType] = field(
        default=None,
        metadata={
            "name": "ToolPosition",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MarkingType(ProcessingType):
    """
    Definition of a marking.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    length_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    interior_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "InteriorAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    style: Optional[MarkingStyleType] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class MortiseType(ProcessingType):
    """
    Definition of a mortise.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length_limited_top: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedTop",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length_limited_bottom: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedBottom",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    shape: Optional[TenonShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShapeRadius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class PocketType(ProcessingType):
    """
    Definition of a pocket.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -179.9,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -179.9,
            "max_inclusive": 179.9,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -179.9,
            "max_inclusive": 179.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    internal_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "InternalAngle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    tilt_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "TiltRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    tilt_end_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "TiltEndSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    tilt_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "TiltOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    tilt_start_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "TiltStartSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    machining_limits: Optional[MachiningLimitType] = field(
        default=None,
        metadata={
            "name": "MachiningLimits",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class ProfileCamberedType(ProcessingType):
    """
    Definition of a profile head cambered.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    max_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    min_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    end_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "EndDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    premill: Optional[PremillType] = field(
        default=None,
        metadata={
            "name": "Premill",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class ProfileFrontType(ProcessingType):
    """
    Definition of a profile front.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    arc_shape: Optional[ArcShapeType] = field(
        default=None,
        metadata={
            "name": "ArcShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    start_rotation: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartRotation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )
    rotation1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rotation1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 180.0,
        }
    )
    radius1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Radius1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    rotation2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rotation2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 180.0,
        }
    )
    radius2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Radius2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class ProfileHeadType(ProcessingType):
    """
    Definition of a profile head.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    arc1: Optional[ProfileArcType] = field(
        default=None,
        metadata={
            "name": "Arc1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    arc2: Optional[ProfileArcType] = field(
        default=None,
        metadata={
            "name": "Arc2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lap_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "LapLength",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    lap_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "LapHeight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class RidgeValleyCutType(ProcessingType):
    """
    Definition of a ridge/valley cut.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    inclination_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "InclinationRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -89.9,
            "max_inclusive": 89.9,
        }
    )
    inclination_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "InclinationOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -89.9,
            "max_inclusive": 89.9,
        }
    )
    start_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "StartLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    end_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "EndLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    angle_ref_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleRefStart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_ref_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleRefEnd",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_opp_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleOppStart",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_opp_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleOppEnd",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )


@dataclass
class RoundArchType(ProcessingType):
    """
    Definition of a round arch.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    camber: Optional[float] = field(
        default=None,
        metadata={
            "name": "Camber",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    arc_shape: Optional[ArcShapeType] = field(
        default=None,
        metadata={
            "name": "ArcShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    premill: Optional[PremillType] = field(
        default=None,
        metadata={
            "name": "Premill",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class SawCutType(ProcessingType):
    """
    Defintion of a saw cut.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    bevel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bevel",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -89.9,
            "max_inclusive": 89.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    tool_position: Optional[ToolPositionType] = field(
        default=None,
        metadata={
            "name": "ToolPosition",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ScarfJointType(ProcessingType):
    """
    Definition of a scarf joint.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 90.0,
        }
    )
    lap_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "LapLength",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    lap_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "LapDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    scarf_shape: Optional[ScarfShapeType] = field(
        default=None,
        metadata={
            "name": "ScarfShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    num_drill_hole: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumDrillHole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0,
            "max_inclusive": 2,
        }
    )
    drill_hole_diam1: Optional[float] = field(
        default=None,
        metadata={
            "name": "DrillHoleDiam1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    drill_hole_diam2: Optional[float] = field(
        default=None,
        metadata={
            "name": "DrillHoleDiam2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class SimpleContourType:
    """
    Defintion of a simple contour (one point and multiple lines and arcs)
    """
    start_point: Optional[PointType] = field(
        default=None,
        metadata={
            "name": "StartPoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    line: List[LineType] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )
    arc: List[ArcType] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "sequential": True,
        }
    )


@dataclass
class SimpleScarfType(ProcessingType):
    """
    Definition of a simple scarf.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_ref_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthRefSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    depth_opp_side: Optional[float] = field(
        default=None,
        metadata={
            "name": "DepthOppSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    num_drill_hole: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumDrillHole",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0,
            "max_inclusive": 2,
        }
    )
    drill_hole_diam1: Optional[float] = field(
        default=None,
        metadata={
            "name": "DrillHoleDiam1",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    drill_hole_diam2: Optional[float] = field(
        default=None,
        metadata={
            "name": "DrillHoleDiam2",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class SlotType(ProcessingType):
    """
    Definition of a slot.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    angle_ref_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleRefPoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    angle_opp_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "AngleOppPoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    add_angle_opp_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "AddAngleOppPoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -179.9,
            "max_inclusive": 179.9,
        }
    )
    machining_limits: Optional[MachiningLimitType] = field(
        default=None,
        metadata={
            "name": "MachiningLimits",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class SphereType(ProcessingType):
    """
    Definition of a sphere.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    start_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartOffset",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )


@dataclass
class StepJointNotchType(ProcessingType):
    """
    Definition of a step joint notch.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    strut_inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "StrutInclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    notch_limited: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "NotchLimited",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    notch_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "NotchWidth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    step_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StepDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    heel_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeelDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    strut_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "StrutHeight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    step_shape: Optional[StepShapeType] = field(
        default=None,
        metadata={
            "name": "StepShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    mortise: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Mortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    mortise_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "MortiseWidth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    mortise_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "MortiseHeight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class StepJointType(ProcessingType):
    """
    Definition of a step joint.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    strut_inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "StrutInclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    step_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StepDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    heel_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeelDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    step_shape: Optional[StepShapeType] = field(
        default=None,
        metadata={
            "name": "StepShape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tenon: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Tenon",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tenon_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "TenonWidth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    tenon_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "TenonHeight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass
class TenonType(ProcessingType):
    """
    Definition of a tenon.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    rotation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    length_limited_top: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedTop",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length_limited_bottom: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "LengthLimitedBottom",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    shape: Optional[TenonShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape_radius: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShapeRadius",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    chamfer: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "Chamfer",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class TextType(ProcessingType):
    """
    Definition of a text.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    alignment_vertical: Optional[AlignmentVerticalType] = field(
        default=None,
        metadata={
            "name": "AlignmentVertical",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    alignment_horizontal: Optional[AlignmentHorizontalType] = field(
        default=None,
        metadata={
            "name": "AlignmentHorizontal",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    alignment_multiline: Optional[AlignmentHorizontalType] = field(
        default=None,
        metadata={
            "name": "AlignmentMultiline",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    stacked_marking: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "StackedMarking",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    text_height_auto: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "TextHeightAuto",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    text_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "TextHeight",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_occurs": 1,
        }
    )


@dataclass
class TriangleCutType(ProcessingType):
    """
    Definition of a triangle cut.
    """
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal1_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal1X",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal1_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal1Y",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal1_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal1Z",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal2_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal2X",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal2_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal2Y",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    normal2_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "Normal2Z",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )


@dataclass
class TyroleanDovetailType(ProcessingType):
    """
    Definition of a tyrolean dovetail.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    cut_off: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "CutOff",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -50000.0,
            "max_inclusive": 50000.0,
        }
    )
    angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.1,
            "max_inclusive": 179.9,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 45.0,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    rebate_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "RebateLength",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": 0.0,
            "max_inclusive": 50000.0,
        }
    )
    lap_position: Optional[EdgePositionType] = field(
        default=None,
        metadata={
            "name": "LapPosition",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lap_exit: Optional[LapExitType] = field(
        default=None,
        metadata={
            "name": "LapExit",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape: Optional[TyroleanDovetailShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    process_side: Optional[ProcessSideType] = field(
        default=None,
        metadata={
            "name": "ProcessSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    frosch: Optional["TyroleanDovetailType.Frosch"] = field(
        default=None,
        metadata={
            "name": "Frosch",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    klingschrot: Optional["TyroleanDovetailType.Klingschrot"] = field(
        default=None,
        metadata={
            "name": "Klingschrot",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class Frosch:
        width: Optional[float] = field(
            default=None,
            metadata={
                "name": "Width",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50000.0,
            }
        )
        depth: Optional[float] = field(
            default=None,
            metadata={
                "name": "Depth",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50000.0,
            }
        )

    @dataclass
    class Klingschrot:
        radius: Optional[float] = field(
            default=None,
            metadata={
                "name": "Radius",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50000.0,
            }
        )
        arc_length: Optional[float] = field(
            default=None,
            metadata={
                "name": "ArcLength",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50000.0,
            }
        )


@dataclass
class VariantType(ProcessingType):
    """
    Definition of a variant.
    """
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    cut_off: Optional[BooleanType] = field(
        default=None,
        metadata={
            "name": "CutOff",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    start_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartX",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartY",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    start_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDepth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    variant_parameter: List[VariantParameterType] = field(
        default_factory=list,
        metadata={
            "name": "VariantParameter",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class DualContourType:
    """
    Definiton of a dual contour (one contour and one associated contour)
    """
    principal_contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "PrincipalContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    associated_contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "AssociatedContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )


@dataclass
class GlueAreaType(ProcessingType):
    """
    Defintion of a glue area.
    """
    contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )


@dataclass
class HouseMortiseType(MortiseType):
    """
    Definition of a house mortise.
    """
    mortise: Optional[MortiseType] = field(
        default=None,
        metadata={
            "name": "Mortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dovetail_mortise: Optional[DovetailMortiseType] = field(
        default=None,
        metadata={
            "name": "DovetailMortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class HouseType(TenonType):
    """
    Definition of a house.
    """
    tenon: Optional[TenonType] = field(
        default=None,
        metadata={
            "name": "Tenon",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dovetail_tenon: Optional[DovetailTenonType] = field(
        default=None,
        metadata={
            "name": "DovetailTenon",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class LockoutAreaType(ProcessingType):
    """
    Defintion of a lockout area.
    """
    contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    for_milling: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForMilling",
            "type": "Attribute",
        }
    )
    for_sawing: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForSawing",
            "type": "Attribute",
        }
    )
    for_nailing: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForNailing",
            "type": "Attribute",
        }
    )
    for_glueing: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForGlueing",
            "type": "Attribute",
        }
    )
    for_planing: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForPlaning",
            "type": "Attribute",
        }
    )
    for_plastering: BooleanType = field(
        default=BooleanType.YES,
        metadata={
            "name": "ForPlastering",
            "type": "Attribute",
        }
    )


@dataclass
class NailContourType(ProcessingType):
    """
    Defintion of a nail contour.
    """
    contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )


@dataclass
class PenContourType(ProcessingType):
    """
    Defintion of a pen contour.
    """
    contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )


@dataclass
class PlaningAreaType(ProcessingType):
    """
    Defintion of a planing area.
    """
    contour: Optional["PlaningAreaType.Contour"] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )

    @dataclass
    class Contour(SimpleContourType):
        depth: Optional[float] = field(
            default=None,
            metadata={
                "name": "Depth",
                "type": "Attribute",
            }
        )


@dataclass
class PlasterAreaType(ProcessingType):
    """
    Defintion of a plaster area.
    """
    contour: Optional["PlasterAreaType.Contour"] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )

    @dataclass
    class Contour(SimpleContourType):
        thickness: Optional[float] = field(
            default=None,
            metadata={
                "name": "Thickness",
                "type": "Attribute",
            }
        )


@dataclass
class BaseContourType:
    """
    Defintion of a base contour (either a contour or a contour with associated
    contour)
    """
    contour: Optional[SimpleContourType] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dual_contour: Optional[DualContourType] = field(
        default=None,
        metadata={
            "name": "DualContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    process: BooleanType = field(
        default=BooleanType.NO,
        metadata={
            "name": "Process",
            "type": "Attribute",
        }
    )


@dataclass
class FreeContourType(ProcessingType):
    """
    Defintion of a free contour.
    """
    contour: Optional["FreeContourType.Contour"] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dual_contour: Optional[DualContourType] = field(
        default=None,
        metadata={
            "name": "DualContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )
    counter_sink: BooleanType = field(
        default=BooleanType.NO,
        metadata={
            "name": "CounterSink",
            "type": "Attribute",
        }
    )
    tool_position: Optional[ToolPositionType] = field(
        default=None,
        metadata={
            "name": "ToolPosition",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Contour(SimpleContourType):
        depth_bounded: BooleanType = field(
            default=BooleanType.NO,
            metadata={
                "name": "DepthBounded",
                "type": "Attribute",
            }
        )
        depth: float = field(
            default=0.0,
            metadata={
                "name": "Depth",
                "type": "Attribute",
                "min_inclusive": 0.0,
            }
        )
        inclination: float = field(
            default=0.0,
            metadata={
                "name": "Inclination",
                "type": "Attribute",
                "min_inclusive": -89.9,
                "max_inclusive": 89.9,
            }
        )


@dataclass
class MillContourType(ProcessingType):
    """
    Defintion of a mill contour.
    """
    contour: Optional["MillContourType.Contour"] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dual_contour: Optional[DualContourType] = field(
        default=None,
        metadata={
            "name": "DualContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )
    counter_sink: BooleanType = field(
        default=BooleanType.NO,
        metadata={
            "name": "CounterSink",
            "type": "Attribute",
        }
    )
    tool_position: Optional[ToolPositionType] = field(
        default=None,
        metadata={
            "name": "ToolPosition",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Contour(SimpleContourType):
        depth_bounded: BooleanType = field(
            default=BooleanType.NO,
            metadata={
                "name": "DepthBounded",
                "type": "Attribute",
            }
        )
        depth: float = field(
            default=0.0,
            metadata={
                "name": "Depth",
                "type": "Attribute",
                "min_inclusive": 0.0,
            }
        )
        inclination: float = field(
            default=0.0,
            metadata={
                "name": "Inclination",
                "type": "Attribute",
                "min_inclusive": -89.9,
                "max_inclusive": 89.9,
            }
        )


@dataclass
class SawContourType(ProcessingType):
    """
    Defintion of a saw contour.
    """
    contour: Optional["SawContourType.Contour"] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dual_contour: Optional[DualContourType] = field(
        default=None,
        metadata={
            "name": "DualContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToolID",
            "type": "Attribute",
        }
    )
    tool_position: Optional[ToolPositionType] = field(
        default=None,
        metadata={
            "name": "ToolPosition",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Contour(SimpleContourType):
        depth_bounded: BooleanType = field(
            default=BooleanType.NO,
            metadata={
                "name": "DepthBounded",
                "type": "Attribute",
            }
        )
        depth: float = field(
            default=0.0,
            metadata={
                "name": "Depth",
                "type": "Attribute",
                "min_inclusive": 0.0,
            }
        )
        inclination: float = field(
            default=0.0,
            metadata={
                "name": "Inclination",
                "type": "Attribute",
                "min_inclusive": -89.9,
                "max_inclusive": 89.9,
            }
        )


@dataclass
class OutlineType(BaseContourType):
    """
    Defintion of an outline.
    """
    apertures: Optional["OutlineType.Apertures"] = field(
        default=None,
        metadata={
            "name": "Apertures",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    reference_plane_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencePlaneID",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        }
    )

    @dataclass
    class Apertures:
        aperture: List[BaseContourType] = field(
            default_factory=list,
            metadata={
                "name": "Aperture",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class ProcessingsType:
    """
    Definition of a machining to be executed on the superior part.
    """
    jack_rafter_cut: List[JackRafterCutType] = field(
        default_factory=list,
        metadata={
            "name": "JackRafterCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    longitudinal_cut: List[LongitudinalCutType] = field(
        default_factory=list,
        metadata={
            "name": "LongitudinalCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    double_cut: List[DoubleCutType] = field(
        default_factory=list,
        metadata={
            "name": "DoubleCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    ridge_valley_cut: List[RidgeValleyCutType] = field(
        default_factory=list,
        metadata={
            "name": "RidgeValleyCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    saw_cut: List[SawCutType] = field(
        default_factory=list,
        metadata={
            "name": "SawCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    slot: List[SlotType] = field(
        default_factory=list,
        metadata={
            "name": "Slot",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    birds_mouth: List[BirdsMouthType] = field(
        default_factory=list,
        metadata={
            "name": "BirdsMouth",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    hip_valley_rafter_notch: List[HipValleyRafterNotchType] = field(
        default_factory=list,
        metadata={
            "name": "HipValleyRafterNotch",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lap: List[LapType] = field(
        default_factory=list,
        metadata={
            "name": "Lap",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    log_house_half_lap: List[LogHouseHalfLapType] = field(
        default_factory=list,
        metadata={
            "name": "LogHouseHalfLap",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    french_ridge_lap: List[FrenchRidgeLapType] = field(
        default_factory=list,
        metadata={
            "name": "FrenchRidgeLap",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    chamfer: List[ChamferType] = field(
        default_factory=list,
        metadata={
            "name": "Chamfer",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    log_house_joint: List[LogHouseJointType] = field(
        default_factory=list,
        metadata={
            "name": "LogHouseJoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    log_house_front: List[LogHouseFrontType] = field(
        default_factory=list,
        metadata={
            "name": "LogHouseFront",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    pocket: List[PocketType] = field(
        default_factory=list,
        metadata={
            "name": "Pocket",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    drilling: List[DrillingType] = field(
        default_factory=list,
        metadata={
            "name": "Drilling",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tenon: List[TenonType] = field(
        default_factory=list,
        metadata={
            "name": "Tenon",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    mortise: List[MortiseType] = field(
        default_factory=list,
        metadata={
            "name": "Mortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    house: List[HouseType] = field(
        default_factory=list,
        metadata={
            "name": "House",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    house_mortise: List[HouseMortiseType] = field(
        default_factory=list,
        metadata={
            "name": "HouseMortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dovetail_tenon: List[DovetailTenonType] = field(
        default_factory=list,
        metadata={
            "name": "DovetailTenon",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dovetail_mortise: List[DovetailMortiseType] = field(
        default_factory=list,
        metadata={
            "name": "DovetailMortise",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    marking: List[MarkingType] = field(
        default_factory=list,
        metadata={
            "name": "Marking",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    text: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    simple_scarf: List[SimpleScarfType] = field(
        default_factory=list,
        metadata={
            "name": "SimpleScarf",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    scarf_joint: List[ScarfJointType] = field(
        default_factory=list,
        metadata={
            "name": "ScarfJoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    step_joint: List[StepJointType] = field(
        default_factory=list,
        metadata={
            "name": "StepJoint",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    step_joint_notch: List[StepJointNotchType] = field(
        default_factory=list,
        metadata={
            "name": "StepJointNotch",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    profile_front: List[ProfileFrontType] = field(
        default_factory=list,
        metadata={
            "name": "ProfileFront",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    profile_cambered: List[ProfileCamberedType] = field(
        default_factory=list,
        metadata={
            "name": "ProfileCambered",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    round_arch: List[RoundArchType] = field(
        default_factory=list,
        metadata={
            "name": "RoundArch",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    planing: List[PlaningType] = field(
        default_factory=list,
        metadata={
            "name": "Planing",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    profile_head: List[ProfileHeadType] = field(
        default_factory=list,
        metadata={
            "name": "ProfileHead",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    sphere: List[SphereType] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    triangle_cut: List[TriangleCutType] = field(
        default_factory=list,
        metadata={
            "name": "TriangleCut",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    tyrolean_dovetail: List[TyroleanDovetailType] = field(
        default_factory=list,
        metadata={
            "name": "TyroleanDovetail",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    dovetail: List[DovetailType] = field(
        default_factory=list,
        metadata={
            "name": "Dovetail",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    free_contour: List[FreeContourType] = field(
        default_factory=list,
        metadata={
            "name": "FreeContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    saw_contour: List[SawContourType] = field(
        default_factory=list,
        metadata={
            "name": "SawContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    mill_contour: List[MillContourType] = field(
        default_factory=list,
        metadata={
            "name": "MillContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    nail_contour: List[NailContourType] = field(
        default_factory=list,
        metadata={
            "name": "NailContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    pen_contour: List[PenContourType] = field(
        default_factory=list,
        metadata={
            "name": "PenContour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    glue_area: List[GlueAreaType] = field(
        default_factory=list,
        metadata={
            "name": "GlueArea",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    planing_area: List[PlaningAreaType] = field(
        default_factory=list,
        metadata={
            "name": "PlaningArea",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    plaster_area: List[PlasterAreaType] = field(
        default_factory=list,
        metadata={
            "name": "PlasterArea",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    lockout_area: List[LockoutAreaType] = field(
        default_factory=list,
        metadata={
            "name": "LockoutArea",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    variant: List[VariantType] = field(
        default_factory=list,
        metadata={
            "name": "Variant",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class ProcessingGroupType(ProcessingType):
    """
    Defintion of a group of processings.
    """
    processings: Optional[ProcessingsType] = field(
        default=None,
        metadata={
            "name": "Processings",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
            "required": True,
        }
    )


@dataclass
class ComponentType:
    """
    Definition of a component.
    """
    transformations: Optional["ComponentType.Transformations"] = field(
        default=None,
        metadata={
            "name": "Transformations",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    outlines: Optional["ComponentType.Outlines"] = field(
        default=None,
        metadata={
            "name": "Outlines",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    user_attributes: Optional["ComponentType.UserAttributes"] = field(
        default=None,
        metadata={
            "name": "UserAttributes",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    colour: Optional[ColourType] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    part_offset: Optional[PartOffsetType] = field(
        default=None,
        metadata={
            "name": "PartOffset",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    grain_direction: Optional["ComponentType.GrainDirection"] = field(
        default=None,
        metadata={
            "name": "GrainDirection",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    reference_side: Optional["ComponentType.ReferenceSide"] = field(
        default=None,
        metadata={
            "name": "ReferenceSide",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    material_class: Optional[MaterialClassType] = field(
        default=None,
        metadata={
            "name": "MaterialClass",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    user_reference_planes: Optional["ComponentType.UserReferencePlanes"] = field(
        default=None,
        metadata={
            "name": "UserReferencePlanes",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    processings: Optional["ComponentType.Processings"] = field(
        default=None,
        metadata={
            "name": "Processings",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    shape: Optional[ShapeType] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    count: int = field(
        default=1,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
            "required": True,
        }
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Attribute",
            "required": True,
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "required": True,
        }
    )
    single_member_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SingleMemberNumber",
            "type": "Attribute",
        }
    )
    assembly_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssemblyNumber",
            "type": "Attribute",
        }
    )
    order_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "OrderNumber",
            "type": "Attribute",
        }
    )
    designation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Designation",
            "type": "Attribute",
        }
    )
    annotation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Annotation",
            "type": "Attribute",
        }
    )
    storey: Optional[str] = field(
        default=None,
        metadata={
            "name": "Storey",
            "type": "Attribute",
        }
    )
    storey_type: Optional[StoreyType] = field(
        default=None,
        metadata={
            "name": "StoreyType",
            "type": "Attribute",
        }
    )
    group: Optional[str] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
        }
    )
    package: Optional[str] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Attribute",
        }
    )
    material: Optional[str] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Attribute",
        }
    )
    timber_grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimberGrade",
            "type": "Attribute",
        }
    )
    quality_grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualityGrade",
            "type": "Attribute",
        }
    )
    planing_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "PlaningLength",
            "type": "Attribute",
        }
    )
    start_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartOffset",
            "type": "Attribute",
        }
    )
    end_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "EndOffset",
            "type": "Attribute",
        }
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
        }
    )
    processing_quality: Optional[ProcessingQualityType] = field(
        default=None,
        metadata={
            "name": "ProcessingQuality",
            "type": "Attribute",
        }
    )
    recess: Optional[RecessType] = field(
        default=None,
        metadata={
            "name": "Recess",
            "type": "Attribute",
        }
    )
    element_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementNumber",
            "type": "Attribute",
        }
    )
    layer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Attribute",
        }
    )
    module_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModuleNumber",
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        }
    )

    @dataclass
    class Transformations:
        transformation: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "Transformation",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Outlines:
        outline: List[OutlineType] = field(
            default_factory=list,
            metadata={
                "name": "Outline",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
                "max_occurs": 3,
            }
        )

    @dataclass
    class UserAttributes:
        user_attribute: List[UserAttributeType] = field(
            default_factory=list,
            metadata={
                "name": "UserAttribute",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class GrainDirection(CoordinateType):
        align: Optional[BooleanType] = field(
            default=None,
            metadata={
                "name": "Align",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ReferenceSide:
        side: Optional[int] = field(
            default=None,
            metadata={
                "name": "Side",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 4,
            }
        )
        align: Optional[BooleanType] = field(
            default=None,
            metadata={
                "name": "Align",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UserReferencePlanes:
        user_reference_plane: List[UserReferencePlaneType] = field(
            default_factory=list,
            metadata={
                "name": "UserReferencePlane",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Processings(ProcessingsType):
        processing_group: List[ProcessingGroupType] = field(
            default_factory=list,
            metadata={
                "name": "ProcessingGroup",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
            }
        )


@dataclass
class CompositeModuleType(ComponentType):
    """
    Definition of a module.
    """
    part_refs: Optional["CompositeModuleType.PartRefs"] = field(
        default=None,
        metadata={
            "name": "PartRefs",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class PartRefs:
        part_ref: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "PartRef",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class PartType(ComponentType):
    """
    Definition of a part.
    """
    camber: Optional[CamberType] = field(
        default=None,
        metadata={
            "name": "Camber",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    alignment: Optional[AlignmentType] = field(
        default=None,
        metadata={
            "name": "Alignment",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )


@dataclass
class RawPartType(ComponentType):
    """
    Definition of a rawpart.
    """
    part_refs: Optional["RawPartType.PartRefs"] = field(
        default=None,
        metadata={
            "name": "PartRefs",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    camber: Optional[CamberType] = field(
        default=None,
        metadata={
            "name": "Camber",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class PartRefs:
        part_ref: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "PartRef",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class CompositeLayerType(CompositeModuleType):
    """
    Definition of a layer.
    """
    module_refs: Optional["CompositeLayerType.ModuleRefs"] = field(
        default=None,
        metadata={
            "name": "ModuleRefs",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class ModuleRefs:
        module_ref: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "ModuleRef",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class CompositeElementType(CompositeLayerType):
    """
    Definition of a element.
    """
    layer_refs: Optional["CompositeElementType.LayerRefs"] = field(
        default=None,
        metadata={
            "name": "LayerRefs",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class LayerRefs:
        layer_ref: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "LayerRef",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class CompositeElementChargeType(CompositeElementType):
    """
    Definition of a elementcharge.
    """
    element_refs: Optional["CompositeElementChargeType.ElementRefs"] = field(
        default=None,
        metadata={
            "name": "ElementRefs",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )

    @dataclass
    class ElementRefs:
        element_ref: List[ReferenceType] = field(
            default_factory=list,
            metadata={
                "name": "ElementRef",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )


@dataclass
class ProjectType:
    """
    Definition of a complete project.

    :ivar user_attributes:
    :ivar rawparts:
    :ivar parts:
    :ivar composites:
    :ivar name:
    :ivar number:
    :ivar guid:
    :ivar section:
    :ivar list_name:
    :ivar customer:
    :ivar architect:
    :ivar editor:
    :ivar delivery_date: in compliance with ISO 8601
    :ivar source_file:
    :ivar processing_quality:
    :ivar recess:
    :ivar comment:
    """
    user_attributes: Optional["ProjectType.UserAttributes"] = field(
        default=None,
        metadata={
            "name": "UserAttributes",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    rawparts: Optional["ProjectType.Rawparts"] = field(
        default=None,
        metadata={
            "name": "Rawparts",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    parts: Optional["ProjectType.Parts"] = field(
        default=None,
        metadata={
            "name": "Parts",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    composites: Optional["ProjectType.Composites"] = field(
        default=None,
        metadata={
            "name": "Composites",
            "type": "Element",
            "namespace": "http://www.design2machine.com",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
    guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUID",
            "type": "Attribute",
            "pattern": r"\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}",
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "name": "Section",
            "type": "Attribute",
        }
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListName",
            "type": "Attribute",
        }
    )
    customer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Customer",
            "type": "Attribute",
        }
    )
    architect: Optional[str] = field(
        default=None,
        metadata={
            "name": "Architect",
            "type": "Attribute",
        }
    )
    editor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Editor",
            "type": "Attribute",
        }
    )
    delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Attribute",
        }
    )
    source_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceFile",
            "type": "Attribute",
        }
    )
    processing_quality: ProcessingQualityType = field(
        default=ProcessingQualityType.AUTOMATIC,
        metadata={
            "name": "ProcessingQuality",
            "type": "Attribute",
        }
    )
    recess: RecessType = field(
        default=RecessType.AUTOMATIC,
        metadata={
            "name": "Recess",
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        }
    )

    @dataclass
    class UserAttributes:
        user_attribute: List[UserAttributeType] = field(
            default_factory=list,
            metadata={
                "name": "UserAttribute",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Rawparts:
        rawpart: List[RawPartType] = field(
            default_factory=list,
            metadata={
                "name": "Rawpart",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Parts:
        part: List[PartType] = field(
            default_factory=list,
            metadata={
                "name": "Part",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Composites:
        modules: Optional["ProjectType.Composites.Modules"] = field(
            default=None,
            metadata={
                "name": "Modules",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
            }
        )
        layers: Optional["ProjectType.Composites.Layers"] = field(
            default=None,
            metadata={
                "name": "Layers",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
            }
        )
        elements: Optional["ProjectType.Composites.Elements"] = field(
            default=None,
            metadata={
                "name": "Elements",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
            }
        )
        element_charges: Optional["ProjectType.Composites.ElementCharges"] = field(
            default=None,
            metadata={
                "name": "ElementCharges",
                "type": "Element",
                "namespace": "http://www.design2machine.com",
            }
        )

        @dataclass
        class Modules:
            module: List[CompositeModuleType] = field(
                default_factory=list,
                metadata={
                    "name": "Module",
                    "type": "Element",
                    "namespace": "http://www.design2machine.com",
                    "min_occurs": 1,
                }
            )

        @dataclass
        class Layers:
            layer: List[CompositeLayerType] = field(
                default_factory=list,
                metadata={
                    "name": "Layer",
                    "type": "Element",
                    "namespace": "http://www.design2machine.com",
                    "min_occurs": 1,
                }
            )

        @dataclass
        class Elements:
            element: List[CompositeElementType] = field(
                default_factory=list,
                metadata={
                    "name": "Element",
                    "type": "Element",
                    "namespace": "http://www.design2machine.com",
                    "min_occurs": 1,
                }
            )

        @dataclass
        class ElementCharges:
            element_charge: List[CompositeElementChargeType] = field(
                default_factory=list,
                metadata={
                    "name": "ElementCharge",
                    "type": "Element",
                    "namespace": "http://www.design2machine.com",
                    "min_occurs": 1,
                }
            )


@dataclass
class Btlx:
    """
    Root element for BTLx data.

    :ivar file_history:
    :ivar project:
    :ivar version: e.g. 1.0 or 1.0.2
    :ivar language: language shortcut in compliance with ISO 639-1
    """
    class Meta:
        name = "BTLx"
        namespace = "http://www.design2machine.com"

    file_history: Optional["Btlx.FileHistory"] = field(
        default=None,
        metadata={
            "name": "FileHistory",
            "type": "Element",
        }
    )
    project: Optional[ProjectType] = field(
        default=None,
        metadata={
            "name": "Project",
            "type": "Element",
            "required": True,
        }
    )
    version: Optional[BtlxVersion] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
        }
    )

    @dataclass
    class FileHistory:
        initial_export_program: Optional[ProgramInfoType] = field(
            default=None,
            metadata={
                "name": "InitialExportProgram",
                "type": "Element",
            }
        )
        editing_program: List[ProgramInfoType] = field(
            default_factory=list,
            metadata={
                "name": "EditingProgram",
                "type": "Element",
            }
        )
