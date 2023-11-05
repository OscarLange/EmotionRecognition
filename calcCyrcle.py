# def isInside(circle_x, circle_y, rad, x, y):

#     # circle_x += 100
#     # circle_y += 100
#     # x += 100
#     # y += 100
     
#     # Compare radius of circle
#     # with distance of its center
#     # from given point
#     if ((x - circle_x) * (x - circle_x) +
#         (y - circle_y) * (y - circle_y) <= rad * rad):
#         return True
#     else:
#         return False


# print(isInside(0.055,0.005,0.375,-0.30092592592592593,-0.017592592592592594))
# print(isInside(0.055,0.005,0.375, 0.03518518518518519,0.3490740740740741))
# print(isInside(0.055,0.005,0.375,0.3907407407407407,0.009259259259259259))
# print(isInside(0.055,0.005,0.375,0.046296296296296294,-0.3435185185185185))

# print(isInside(0.055,0.005,0.375,-0.30092592592592593,-0.017592592592592594))
# print(isInside(0.055,0.005,0.375, 0.03518518518518519,0.3490740740740741))
# print(isInside(0.055,0.005,0.375,0.3907407407407407,0.009259259259259259))
# print(isInside(0.055,0.005,0.375,0.046296296296296294,-0.3435185185185185))

def cross_prod(x1, y1, x2, y2):
    return x1*y2 - x2*y1

