from shadow import *

__import__("logging").getLogger("parso.python.diff").setLevel("INFO")
__import__("logging").getLogger("parso.cache").setLevel("INFO")
__import__("logging").getLogger("asyncio").setLevel("INFO")



# Initialize a graphical display window (from ifcos)

setting=ifcopenshell.geom.settings()
setting.set(setting.USE_PYTHON_OPENCASCADE, True)

filename='C:/Users/cvoivret/source/canopia_ifcocc/data/DCE_CDV_BAT.ifc'

rsv=rtaa_ventilation_study(filename)
lgt4b=[499,705,731,757,783,809,859]


rsv.add_space_elements(lgt4b,[])#,['IfcSpace'])
rsv.add_opening_elements([],['IfcWindow','IfcDoor'])
rsv.set_geometries()
rsv.run()
rsv.display()