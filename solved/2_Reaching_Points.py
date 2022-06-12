class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>=sx and ty>=sy:
            if sx==tx and sy==ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx%=ty
                else:
                    return (tx-sx)%ty==0
            else:
                if tx > sx:
                    ty%=tx
                else:
                    return (ty-sy)%tx==0
        return sx==tx and sy==ty