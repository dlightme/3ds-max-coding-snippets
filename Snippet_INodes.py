from dataclasses import dataclass , asdict
import pymxs
mxs = pymxs.runtime

@dataclass
class polyobjData:
    sNodeName: str
    iVertCount: int
    dVertCoords: dict
    iInode: int = 1

def objList2transform():
        nodehandles = []
        for obj in mxs.objects:
            if mxs.classOf(obj) == mxs.Editable_mesh or mxs.classOf(obj) == mxs.Editable_Poly:
                nodehandles.append(obj.INode.handle)
        return(nodehandles)

def main():
    """ Main entry point of the app """
    nodehandles = objList2transform()
    
    #d = {}
    
    for INode in nodehandles:
        name = mxs.maxOps.getNodeByHandle(INode)
        #print(INode)
        INode = polyobjData(name, 1, INode)
        print(INode)
        
    
    
if __name__ ==  "__main__":
	""" This is executed when run from the command line """
	main()
