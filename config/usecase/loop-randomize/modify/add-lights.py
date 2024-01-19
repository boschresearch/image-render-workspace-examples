import bpy

if __name__ == "__main__":
    sName = "Light"
    fEnergy = 1000
    lPosition = [0, 0, 0]
# endif

xLight = bpy.data.lights.new(name=sName, type="POINT")
xLight.energy = fEnergy

objLight = bpy.data.objects.new(name=sName, object_data=xLight)

bpy.context.collection.objects.link(objLight)
objLight.location = lPosition
