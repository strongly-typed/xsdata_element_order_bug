from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from btlx.btlx_11 import Btlx

filename = 'tests/mill_line_arc.btlx'
parser = XmlParser(context=XmlContext())

btlx = parser.parse(filename, Btlx)

contour = btlx.project.parts.part[0].processings.mill_contour[0].contour

context = XmlContext()
meta = context.fetch(contour.__class__)

for var, value in XmlSerializer.next_value(contour, meta):
    print(value)
