import cv2
import numpy as np

def track_roi(rois, prev_img, curr_img, tracker):
	# rois is a list of rois
	# previous and current image frames are prev_img and curr_img
	# tracker is the type of tracking algorithm to be used

	OPENCV_OBJECT_TRACKERS = {
		"csrt": cv2.TrackerCSRT_create,
		"kcf": cv2.TrackerKCF_create,
		"boosting": cv2.TrackerBoosting_create,
		"mil": cv2.TrackerMIL_create,
		"tld": cv2.TrackerTLD_create,
		"medianflow": cv2.TrackerMedianFlow_create,
		"mosse": cv2.TrackerMOSSE_create
	}

	tracker = OPENCV_OBJECT_TRACKERS[tracker]
	
 