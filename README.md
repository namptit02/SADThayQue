# Cách cài đặt mỗi app một db(App Cart Mysql, app Product MongoDB)
B1: Chỉnh sửa phần DATABASE trong file djangob12/settings.by như sau:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mysql': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': 'baitap1',
        'USER': 'root',
        'PASSWORD': 'dienpassvao',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': 'baitap1',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
    }
        
    }
    
}

B2: Chạy các lệnh sau để cập nhâ lại thông tin: 
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --database=mysql
python manage.py migrate --database=mongodb

B3: Trong app cart và product, mỗi app tạo 1 file dbRouter.py
Ví dụ file dbRouter.py trong app Cart:
class CartDBRouter(object):
    route_app_labels = {'cart'}
    db_name = 'mysql'

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None
        
B4: Mở lại file djangob12/settings.py bổ sung thêm dòng sau:
DATABASE_ROUTERS = ["cart.dbRouter.CartDBRouter", "product.dbRouter.ProductDBRouter"]
