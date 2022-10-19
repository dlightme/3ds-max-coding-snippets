import pymxs
mxs = pymxs.runtime

#coll = mxs.select(mxs.objects)
#mxs.classOf(mxs.selection[0])

for obj in mxs.objects:
	#items = obj.GetObject()
	if mxs.classOf(obj) == mxs.Physical:
		print("Camera")		
	
#node = mxs.getCurrentSelection()[0]

for obj in mxs.objects:
	#items = obj.GetObject()
	if mxs.classOf(obj) == mxs.Editable_mesh or mxs.classOf(obj) == mxs.Editable_Poly:
		print("Editable Mesh found : ", obj.name)
	


