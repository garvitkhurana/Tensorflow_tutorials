import tensorflow as tf

# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)


result = x1*x2
result=tf.multiply(x1,x2)

print(result)

# defines our session and launches graph
sess = tf.Session()
# runs result
print(sess.run(result))
sess.close()

## other way
with tf.Session() as session:
    ans=session.run(result)
    print(ans)