from typing import List
from kiosk_app.models.FoodItem import FoodItem
from kiosk_app.models.ToppingVariant import Topping, Variant
from kiosk_app.models.EnumClasses import OrderStatus, PaymentMethod


class OrderItem:
    def __init__(self, foodItem: FoodItem, quantity: int, note: str, evoucherTangMonId: int = None, toppingList:List[Topping] = [], variantList:List[Variant] = [], is_free = False):
        self.foodItem=foodItem #mỗi 1 OrderItem sẽ tương ứng với 1 FoodItem
        self.quantity=quantity #Kèm theo đó là một số thuộc tính khác.
        self.evoucherTangMonId = evoucherTangMonId
        self.toppingList= toppingList
        self.variantList = variantList
        self.note=note
        self.is_free=is_free
        self.total_item_price = self.calculate_item_price()

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(food_item={self.foodItem.__repr__()!r}, quantity={self.quantity!r}), is_free={self.is_free!r})')

    def __eq__(self, other):
        if isinstance(other, OrderItem): #Function này giúp ta biết được 2 object OrderItem sẽ bằng nhau khi nào. Define function sẽ hiện thực hoá phần so sánh các món có trong giỏ hàng -> chức năng tăng số lượng của một món đã tồn tại trong giỏ hàng nếu món mới được khách thêm giống y đúc.
            return self.foodItem == other.foodItem and self.evoucherTangMonId == other.evoucherTangMonId and self.toppingList == other.toppingList and self.variantList == other.variantList and self.note == other.note and self.is_free == other.is_free

    def calculate_item_price(self):
        item_price = 0
        for topping in self.toppingList:
            item_price += topping.discountPrice*self.quantity
        for variant in self.variantList:
            item_price += variant.price*self.quantity
        item_price += self.foodItem.discounted_price * self.quantity
        return item_price

class Order:
    """Đây là class quản lý giỏ hàng, đơn hàng."""
    def __init__(self):
        self.id = None #cập nhật ID sau khi đã submit order vào database
        self.paymentMethod: PaymentMethod = PaymentMethod.cash #Sử dụng enum để pick ra giá trị dạng số của payment method (VD: tiền mặt là cash -> số 1)
        self.isDineIn = True
        self.totalAmount = 0
        self.totalPrice = 0 #Tổng tiền (trước khi giảm từ evoucher)
        self.evoucherDiscount = 0 #Giảm từ evoucher
        self.orderItems: List[OrderItem] = []
        self.isAppliedVoucher = False
        self.evoucherGiamGiaId = None
        self.orderStatus = OrderStatus.unpaid
        self.init_calculate_totals()

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(cart_items_amount={self.totalAmount!r}, total_price={self.totalPrice!r})')

    def init_calculate_totals(self):
        cart_length = len(self.orderItems)
        if cart_length > 0:
            self.totalAmount = 0
            self.totalPrice = 0
            for order_item in self.orderItems:
                self.totalAmount += order_item.quantity
                self.totalPrice += order_item.total_item_price

    def add_new_order_items(self, orderItems: List[OrderItem]):
        """Sử dụng hàm này để thêm món mới vào đơn hàng. Nó sẽ tự động tính lại giá tổng và số lượng của đơn hàng."""
        for orderItem in orderItems:
            self.orderItems.append(orderItem)
            self.totalAmount += orderItem.quantity
            print(f"Added {orderItem.quantity}")
            self.totalPrice += orderItem.total_item_price

    def update_evoucher_discount(self, isPercent: bool, discountValue: int, minimumPrice: int, maximumDiscount: int):
        """Sử dụng function này sau khi người dùng bấm áp dụng voucher giảm giá, check được trong hệ thống hợp lệ
        :return : bool"""
        if self.totalPrice < minimumPrice:
            return False #Chưa đủ điều kiện áp dụng
        if isPercent:
            tempDiscount = self.totalPrice*(discountValue/100)
        else:
            tempDiscount = discountValue
        if tempDiscount > maximumDiscount:
            self.evoucherDiscount = maximumDiscount
        else:
            self.evoucherDiscount = tempDiscount
        self.isAppliedVoucher = True
        return True #Đã áp dụng mã giảm

    def remove_order_item(self, Item: object):
        """Hàm xoá order item trên giỏ hàng
        :param : obj cần xoá"""
        for item in self.orderItems:
            if item == Item:
                self.orderItems.remove(item)








