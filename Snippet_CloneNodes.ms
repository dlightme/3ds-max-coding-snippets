--  maxOps.CloneNodes <&node array>nodes offset:<point3> expandHierarchy:<boolean> cloneType:<enum> actualNodeList:<&node array> newNodes:<&node array> 
-- -- variables passed by reference without initializing, works right
-- maxops.clonenodes s actualNodeList:&c newNodes:&d
-- c --> #($sphere01)
-- d --> #($sphere03)
a = selection
maxOps.CloneNodes a newNodes:&newnodes -- actualNodeList:&existing not required argument

select newnodes
