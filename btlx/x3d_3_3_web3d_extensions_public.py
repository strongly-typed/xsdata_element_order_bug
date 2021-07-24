from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from btlx.x3d_3_3 import (
    Is,
    MetadataDouble,
    MetadataFloat,
    MetadataInteger,
    MetadataSet,
    MetadataString,
)

__NAMESPACE__ = "http://www.design2machine.com"


class XvlShellShellTypes(Enum):
    POLYGON_MESH = "POLYGON_MESH"
    LATTICE_MESH = "LATTICE_MESH"


@dataclass
class XvlShell:
    class Meta:
        namespace = "http://www.design2machine.com"

    is_value: Optional[Is] = field(
        default=None,
        metadata={
            "name": "IS",
            "type": "Element",
        }
    )
    metadata_double: Optional[MetadataDouble] = field(
        default=None,
        metadata={
            "name": "MetadataDouble",
            "type": "Element",
        }
    )
    metadata_float: Optional[MetadataFloat] = field(
        default=None,
        metadata={
            "name": "MetadataFloat",
            "type": "Element",
        }
    )
    metadata_integer: Optional[MetadataInteger] = field(
        default=None,
        metadata={
            "name": "MetadataInteger",
            "type": "Element",
        }
    )
    metadata_set: Optional[MetadataSet] = field(
        default=None,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
        }
    )
    metadata_string: Optional[MetadataString] = field(
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
    shell_type: Optional[XvlShellShellTypes] = field(
        default=None,
        metadata={
            "name": "shellType",
            "type": "Attribute",
        }
    )
    number_of_divisions: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfDivisions",
            "type": "Attribute",
        }
    )
    vertex_round: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertexRound",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    edge_begin_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "edgeBeginCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    edge_end_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "edgeEndCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    edge_round: Optional[str] = field(
        default=None,
        metadata={
            "name": "edgeRound",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*(([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    edge_begin_vector: Optional[str] = field(
        default=None,
        metadata={
            "name": "edgeBeginVector",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    edge_end_vector: Optional[str] = field(
        default=None,
        metadata={
            "name": "edgeEndVector",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s+){2}([+-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([Ee][+-]?[0-9]+)?)\s*,?\s*)*",
        }
    )
    face_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "faceCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    face_tex_coord_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "faceTexCoordIndex",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"(\s)*([+-]?(0|[1-9][0-9]*)([Ee][+-]?[0-9]+)?\s*,?\s*)*",
        }
    )
    face_empty: Optional[str] = field(
        default=None,
        metadata={
            "name": "faceEmpty",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    face_hidden: Optional[str] = field(
        default=None,
        metadata={
            "name": "faceHidden",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\s*((true|false)\s*,?\s*)*",
        }
    )
    container_field: str = field(
        default="geometry",
        metadata={
            "name": "containerField",
            "type": "Attribute",
        }
    )
