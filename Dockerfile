FROM python:3.11-slim

# جلوگیری از cacheهای اضافی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی سورس‌کد
COPY . .

# پورت API
EXPOSE 8000

# اجرای API
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
