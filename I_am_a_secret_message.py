# remove X

garbled_1 = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message_1 = filter(lambda x: x != "X", garbled_1)
print message_1

# extract the message

garbled_2 = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

string = garbled_2[::-1]
message_2 = string[::2]

print message_2
