from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field, user_username

class CustomAccountAdapter(DefaultAccountAdapter):
 
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        gender = data.get("gender")
        phone_number = data.get("phone_number")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        # financial_product = data.get("financial_products")
        
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if email:
            user_field(user, "email", email)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user_field(user, "gender", gender)
        if phone_number:
            user.phone_number = phone_number
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
       
        # if financial_product:
        #     financial_products = user.financial_products.split(',')
        #     financial_products.append(financial_product)
       
        #     if len(financial_products) > 1:
        #         financial_products = ','.join(financial_products)
        #     user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
        # Ability not to commit makes it easier to derive from
        # this adapter by adding
            user.save()
        return user
