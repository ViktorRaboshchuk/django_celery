# django_celery

This is simple project that runs one task using Celery and Redis. You can see task running using command:

```
celery --broker=redis://localhost:6379/0 flower
```
