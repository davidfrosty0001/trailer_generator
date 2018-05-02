from moviepy.editor import *  
import csv
import operator
from collections import OrderedDict
from operator import itemgetter
import sys
from sys import stdout
import os

interval = 5
video_orginal = VideoFileClip("Frozen.mp4")
output_dir    = 'frozen_clip'
for index in range(6800 / interval):
	try:
		video0 = video_orginal.subclip(5 * index, 5 * (index + 1 ))
	except:
		break
	# final_clip = concatenate_videoclips([final_clip, video1])
	clip_resized = video0.resize(width=360, height=142)
	clip_resized.write_videofile(os.path.join(output_dir, "%s.mp4" % str(index)),fps=15)
	stdout.write("%s written to disk!" % str(index))
	stdout.flush()


# for key, value in timezone.iteritems():
# 	video = VideoFileClip("evergarden_ep4.mp4").subclip(5 * key, 5 * key + 1)
# 	final_clip = concatenate_videoclips([clip1,clip2,clip3])


