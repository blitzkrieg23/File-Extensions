x = input("Enter the filename and filetype:")
x = x.lower().strip()

if x.endswith((".jpg", ".jpeg")):
    print("image/jpeg")

elif x.endswith(".gif"):
    print("image/gif")

elif x.endswith (".png"):
    print("image/png")

elif x.endswith (".zip"):
    print("application/zip")

elif x.endswith (".pdf"):
    print("application/pdf")

elif x.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")