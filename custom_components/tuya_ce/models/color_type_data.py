from dataclasses import dataclass, field

from homeassistant.components.tuya import DPCode

from .base import IntegerTypeData


@dataclass
class ColorTypeData:
    # Color Type Data.

    h_type: IntegerTypeData
    s_type: IntegerTypeData
    v_type: IntegerTypeData
    
    
@dataclass
class ColorTypes:
    
    DEFAULT_COLOR_TYPE_DATA = ColorTypeData(
        h_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=360, step=1),
        s_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=255, step=1),
        v_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=255, step=1),
)

    DEFAULT_COLOR_TYPE_DATA_V2 = ColorTypeData(
        h_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=360, step=1),
        s_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=1000, step=1),
        v_type=IntegerTypeData(DPCode.COLOUR_DATA_HSV, min=1, scale=0, max=1000, step=1),
)
