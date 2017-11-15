# classes and subclasses to import
import cv2
import numpy as np
import os

filename = 'results1A_TeamId.csv'


#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
# subroutine to write results to a csv
def writecsv(color, shape, (cx, cy)):
    global filename
    # open csv file in append mode
    filep = open(filename, 'a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + str(cx) + "-" + str(cy)
    # write to csv
    filep.write(datastr)


def main(path):
    #####################################################################################################
    # Write your code here!!!
    #####################################################################################################
    toReturn = []
    toReturn.append(str(path)[2:])
    print toReturn
    img = cv2.imread(path)
    # cv2.imshow('image', img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # **************************************************
    # red = np.uint8([[[0, 0, 255]]])
    # hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    # print hsv_red
    # define range of red color in HSV
    lower_red = np.array([0, 255, 255])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)

    grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(grey, 127, 255, cv2.THRESH_OTSU)

    cv2.imshow('thresRED', thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        color = "Red"
        size = np.size(cnt)
        sumX = 0
        sumY = 0
        for x in cnt:
            sumX = sumX + x[0][0]
            sumY = sumY + x[0][1]

        CentroidX = sumX / size
        CentroidY = sumY / size

        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 5:
            shape = "Pentagon"
            cv2.drawContours(img, [cnt], 0, 255, -1)
        elif len(approx) == 3:
            shape = "Triangle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        elif len(approx) == 4:
            shape = "Square"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) == 6:
            shape = "Hexagon"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) >= 15:
            shape = "Circle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)

        toReturn.append(["%s-%s-%d-%d" % (color, shape, CentroidX, CentroidY)])

    print toReturn

    # **************************************************
    green = np.uint8([[[0, 128, 0]]])
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    # print hsv_green
    # define range of green color in HSV
    lower_green = np.array([50, 255, 128])
    upper_green = np.array([70, 255, 128])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)

    grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(grey, 127, 255, cv2.THRESH_OTSU)

    cv2.imshow('thresGREEN', thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        color = "Green"
        size = np.size(cnt)
        sumX = 0
        sumY = 0
        for x in cnt:
            sumX = sumX + x[0][0]
            sumY = sumY + x[0][1]

        CentroidX = sumX / size
        CentroidY = sumY / size

        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 5:
            shape = "Pentagon"
            cv2.drawContours(img, [cnt], 0, 255, -1)
        elif len(approx) == 3:
            shape = "Triangle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        elif len(approx) == 4:
            shape = "Square"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) == 6:
            shape = "Hexagon"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) >= 15:
            shape = "Circle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)

        toReturn.append(["%s-%s-%d-%d" % (color, shape, CentroidX, CentroidY)])

    print toReturn

    # **************************************************
    blue = np.uint8([[[255, 0, 0]]])
    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    # print hsv_blue
    # define range of blue color in HSV
    lower_blue = np.array([110, 255, 255])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)

    grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(grey, 127, 255, cv2.THRESH_OTSU)

    cv2.imshow('thresBLUE', thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('contoursBLUE', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for cnt in contours:
        color = "Blue"
        size = np.size(cnt)
        sumX = 0
        sumY = 0
        for x in cnt:
            sumX = sumX + x[0][0]
            sumY = sumY + x[0][1]

        CentroidX = sumX / size
        CentroidY = sumY / size

        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 5:
            shape = "Pentagon"
            cv2.drawContours(img, [cnt], 0, 255, -1)
        elif len(approx) == 3:
            shape = "Triangle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        elif len(approx) == 4:
            shape = "Square"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) == 6:
            shape = "Hexagon"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
        elif len(approx) >= 15:
            shape = "Circle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)

        toReturn.append(["%s-%s-%d-%d" % (color, shape, CentroidX, CentroidY)])

    print toReturn

    return toReturn


#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
# main where the path is set for the directory containing the test images
if __name__ == "__main__":
    global filename
    mypath = '.'
    # getting all files in the directory
    onlyfiles = ["./%s" % (f,) for f in os.listdir(mypath) if f.endswith(".png")]
    print onlyfiles
    # iterate over each file in the directory
    for fp in onlyfiles:
        # Open the csv to write in append mode
        filep = open('results_TeamId.csv', 'a')
        # this csv will later be used to save processed data, thus write the file name of the image
        filep.write(fp)
        # close the file so that it can be reopened again later
        filep.close()
        # process the image
        data = main(fp)
        print data
        # open the csv
        filep = open(filename, 'a')
        # make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        # close the file
        filep.close()
