import tensorflow as tf

# creates nodes in a graph
# "construction phase"



x = tf.constant(5)
y = tf.constant(6)


'''----------------------------------------------------------------------'''
## other way

x=tf.Variable(5,name="x")
y=tf.Variable(6,name="y")


result = x*y
## other way
result=tf.multiply(x,y)

print(result)

# defines our session and launches graph
sess = tf.Session()
# runs result
sess.run(x.initializer)
sess.run(y.initializer)
print(sess.run(result))
sess.close()

'''----------------------------------------------------------------------'''

## other way
with tf.Session() as session:
    tf.global_variables_initializer().run()
    ans=session.run(result)
    print(ans)

'''----------------------------------------------------------------------'''

w = tf.constant(3) 
x=w+2 
y=x+5 
z=x*3
with tf.Session() as sess: 
    print(sess.run(y))
    print(z.eval()) ## other way
    file_writer=tf.summary.FileWriter("/Users/garvitkhurana/Desktop/grp",sess.graph)


'''----------------------------------------------------------------------'''

