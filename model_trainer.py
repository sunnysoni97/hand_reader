import tensorflow as tf
import input_data

def create_model(data, weight, bias):
	y = tf.nn.softmax(tf.matmul(data,weight)+bias)
	return y

def train_data():
	mnist = input_data.read_data_sets("mnist_data/",one_hot=True)
	x = tf.placeholder("float",[None,784])
	w = tf.Variable(tf.zeros([784,10]), name="weights")
	b = tf.Variable(tf.zeros([10]), name="biases")

	y = create_model(x,w,b)
	y1 = tf.placeholder("float",[None,10])

	cross_entropy = -tf.reduce_sum(y1*tf.log(y))

	train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
	init = tf.initialize_all_variables()
	sess = tf.Session()
	saver = tf.train.Saver()
	sess.run(init)

	for i in range(15000):
		batch_xs, batch_ys = mnist.train.next_batch(20)
		sess.run(train_step, feed_dict={x:batch_xs, y1:batch_ys})

	saver.save(sess, './model_final/model_final')

	correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y1,1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	print ("The Model is trained with the accuracy : ")
	print (sess.run(accuracy, feed_dict={x:mnist.test.images, y1:mnist.test.labels}))