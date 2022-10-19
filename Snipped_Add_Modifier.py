##### Attempting to use a modifier ##########
Define"Edit Poly" Modfier
modEP = mxs.Edit_Poly()

# Add Editable Poly Modfier
mxs.addModifier(box1, modEP)

#Set Subobect model to Vertex 
modEP.SetEPolySelLevel(1)

box1.GetNumVerticesnode(modEP) # Maxscript $.GetNumVerticesnode: node syntax. Node: $PolyMesh:NewBox
box1.GetSelection()  #doens't work 