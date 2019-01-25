import tensorflow as tf
import numpy as np
import image_processor as ip
import model_trainer as mt

def find_no(val_ary):
	max=val_ary[0][0]
	no=0
	for i in range(10):
		if(val_ary[0][i] > max):
			max = val_ary[0][i]
			no=i
	return no

def calculate_image(fileName):
	tf.reset_default_graph()
	imp_meta = tf.train.import_meta_graph('./model_final/model_final.meta')
	sess = tf.Session()
	imp_meta.restore(sess, tf.train.latest_checkpoint('./model_final/'))
	x = tf.placeholder("float",[None,784])
	w = sess.run('weights:0')
	b = sess.run('biases:0')
	y = mt.create_model(x,w,b)
	img = ip.convert_to_mnist(fileName)
	img = img.flatten()
	img_ary = np.zeros((1,784))
	img_ary[0] = img
	val_ary = y.eval(feed_dict={x:img_ary}, session=sess)
	return(find_no(val_ary))