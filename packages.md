### پکیج **pylint-django**

**pylint-django** یک افزونه برای ابزار تحلیل کد **Pylint** است که به طور ویژه برای پروژه‌های Django طراحی شده و قابلیت‌های زیر را فراهم می‌کند:
- پشتیبانی از ساختارهای Django مانند مدل‌ها، نماها، و فرم‌ها.
- کاهش هشدارهای نادرست (False Positives).
- بهبود دقت تحلیل کد با افزودن قوانین مخصوص به Django.
- سازگاری با استانداردهای کدنویسی Django.

### پکیج **django-waffle**

**django-waffle** ابزاری برای مدیریت **Feature Flags** است. امکانات اصلی:
- مدیریت پرچم‌های ویژگی (Feature Flags).
- استفاده از Switches و Samples برای کنترل انتشار ویژگی‌ها.
- پیاده‌سازی آزمایش‌های A/B.
- مدیریت و مشاهده پرچم‌ها از طریق پنل مدیریت Django.

### پکیج **django-stubs**

**django-stubs** افزونه‌ای برای Mypy است که تایپ‌های استاتیک را به پروژه‌های Django اضافه می‌کند. ویژگی‌ها:
- تایپ‌گذاری دقیق برای مدل‌ها، نماها، و فرم‌ها.
- شناسایی خطاهای تایپی پیش از اجرا.
- ادغام با Mypy و IDE‌ها برای بهبود تجربه توسعه‌دهنده.

### پکیج **django-silk**

**django-silk** ابزاری برای پروفایلینگ و نظارت بر عملکرد پروژه‌های Django است. ویژگی‌ها:
- پروفایلینگ درخواست‌ها، پاسخ‌ها، و کوئری‌های پایگاه داده.
- بررسی زمان اجرای Viewها و کوئری‌های کند.
- ارائه پنل مدیریتی برای تحلیل داده‌های پروفایلینگ.

### پکیج **django-compat**

**django-compat** ابزاری برای جلوگیری از ناسازگاری بین نسخه‌های مختلف Django است. ویژگی‌ها:
- پشتیبانی از نسخه‌های مختلف Django.
- ارائه توابع جایگزین برای APIهای قدیمی یا جدید.
- کاهش خطاهای ناسازگاری هنگام مهاجرت به نسخه‌های جدید.

### پکیج **django-model-utils**

**django-model-utils** ابزارهایی برای توسعه مدل‌های پیشرفته در Django ارائه می‌دهد:
- **TimeStampedModel**: افزودن فیلدهای `created` و `modified` به مدل‌ها.
- **SoftDeletableModel**: حذف نرم (Soft Delete).
- **StatusModel**: مدیریت وضعیت رکوردها.
- **FieldTracker**: دنبال کردن تغییرات فیلدها.

### پکیج **django-countries**

**django-countries** برای افزودن فیلدهای کشور به مدل‌ها و فرم‌ها استفاده می‌شود:
- ارائه لیست استاندارد کشورها (ISO 3166-1).
- پشتیبانی از پرچم‌ها و ترجمه نام کشورها.
- فیلدهای فرم و ویجت‌های پیش‌ساخته.

### پکیج **django-simple-history**

**django-simple-history** ابزاری برای ذخیره تاریخچه تغییرات مدل‌های Django است:
- ثبت خودکار تغییرات در مدل‌های مشخص‌شده.
- مشاهده و بازگرداندن نسخه‌های قبلی رکوردها.
- یکپارچگی با Django Admin.

### پکیج **django-polymorphic**

**django-polymorphic** برای مدیریت مدل‌های چندریختی (Polymorphic Models) در Django استفاده می‌شود:
- QuerySet‌های چندریختی.
- پشتیبانی از وراثت چندریختی.
- مدیریت ساده داده‌ها در معماری‌های پیچیده.

### پکیج **django-localflavor**

**django-localflavor** مجموعه‌ای از ابزارها و اعتبارسنجی‌های خاص کشورها است:
- فیلدهای فرم و اعتبارسنجی شماره تلفن، کد پستی و غیره.
- پشتیبانی از کشورهای متعدد.

### پکیج **django-modelcluster**

**django-modelcluster** ابزاری برای مدیریت مدل‌های مرتبط در Django است:
- مدیریت داده‌های مرتبط در حافظه.
- پشتیبانی از فرم‌های inline در Admin.
- مناسب برای Wagtail CMS.

### پکیج **django-redis-cache**

**django-redis-cache** برای استفاده از Redis به عنوان سیستم کش Django استفاده می‌شود:
- پیکربندی ساده Redis برای کش.
- مدیریت TTL (زمان انقضا).
- پشتیبانی از Sentinel و Clustering.

### پکیج **django-appconf**

**django-appconf** ابزاری برای مدیریت تنظیمات اپلیکیشن‌های Django است:
- تعریف تنظیمات پیش‌فرض اپلیکیشن.
- پشتیبانی از تنظیمات سفارشی در پروژه.
- جداسازی تنظیمات اپلیکیشن از تنظیمات اصلی پروژه.

### پکیج **django-braces**

**django-braces** مجموعه‌ای از Mixin‌های آماده برای مدیریت Viewهای Django است:
- **LoginRequiredMixin**: بررسی ورود کاربر.
- **PermissionRequiredMixin**: بررسی مجوزها.
- **CsrfExemptMixin**: غیرفعال کردن CSRF.
- کاهش کدنویسی تکراری و افزایش خوانایی.

### پکیج **django-annoying**

**django-annoying** مجموعه‌ای از میانبرها و ابزارهای مفید برای توسعه پروژه‌های Django است:
- **SingletonModel**: مدیریت مدل‌های Singleton.
- **ajax_request**: مدیریت پاسخ‌های JSON.
- **get_object_or_None**: بازگرداندن None به جای خطای 404.

### پکیج **django-prometheus**

**django-prometheus** ابزاری برای مانیتورینگ متریک‌ها در پروژه‌های Django است:
- جمع‌آوری داده‌های مربوط به درخواست‌ها، پایگاه داده و کش.
- ارائه متریک‌ها در یک endpoint برای Prometheus.
- امکان تعریف متریک‌های سفارشی.

### پکیج **django-tables2**

**django-tables2** برای ساخت جداول HTML در Django استفاده می‌شود:
- ایجاد جداول قابل مرتب‌سازی و صفحه‌بندی‌شده.
- ادغام با QuerySet‌ها و مدل‌های Django.
- استفاده از قالب‌های استاندارد مانند Bootstrap.

### پکیج **django-fsm**

**django-fsm** برای مدیریت ماشین حالت محدود در Django استفاده می‌شود:
- تعریف حالت‌ها و انتقالات در مدل‌ها.
- افزودن قوانین و شرایط به انتقالات.
- نمایش وضعیت مدل‌ها در Admin.

### پکیج **django-heroku**

**django-heroku** ابزاری برای پیکربندی خودکار پروژه‌های Django در پلتفرم Heroku است:
- تنظیم خودکار پایگاه داده PostgreSQL.
- مدیریت فایل‌های استاتیک.
- بهینه‌سازی تنظیمات لاگ‌ها و کش.

### پکیج **django-sekizai**

**django-sekizai** ابزاری برای مدیریت بلوک‌های پویا در قالب‌های Django است:
- افزودن محتوا به بخش‌های مختلف قالب (CSS و JavaScript).
- کاهش تکرار کد در قالب‌ها.
- سازگاری با سیستم قالب Django.

