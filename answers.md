# Part 1
## 1.01
```$ kubectl logs first-deployment-58dcf4566d-wp7ns | head -n 5
2021-02-04 07:22:05,533: a93f9008-562d-496a-a704-97affdf920a1
2021-02-04 07:22:10,537: a93f9008-562d-496a-a704-97affdf920a1
2021-02-04 07:22:15,541: a93f9008-562d-496a-a704-97affdf920a1
2021-02-04 07:22:20,543: a93f9008-562d-496a-a704-97affdf920a1
2021-02-04 07:22:25,548: a93f9008-562d-496a-a704-97affdf920a1
```

## 1.02
Decided to leverage Flask's built in logging when starting the server.
```$ kubectl logs -f todo-8447c4645d-dwzsd
 * Serving Flask app "todo/hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
