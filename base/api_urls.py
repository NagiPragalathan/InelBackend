from rest_framework.routers import DefaultRouter
from base import api_views

router = DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'posts', api_views.PostViewSet)
router.register(r'career', api_views.CareerFormViewSet)
router.register(r'contact', api_views.ContactInquiryViewSet)
router.register(r'aftermarket', api_views.AftermarketFormViewSet)
router.register(r'vehicle-categories', api_views.VehicleCategoryViewSet)
router.register(r'product-types', api_views.ProductTypeViewSet)
router.register(r'products', api_views.ProductViewSet)

app_name = 'api'
