import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex

# ملاحظة: إذا كنتِ تستخدمين مكتبة معينة للذكاء الاصطناعي مثل google-generativeai
# فسوف تحتاجين للتأكد من كتابتها في الإعدادات، هنا سنصنع الواجهة الذكية لكِ ولصديقتكِ.

class TikTokAssistantApp(App):
    def build(self):
        # العنوان الأساسي للتطبيق
        self.title = "مساعد تيك توك الوردي الذكي 🎀"
        
        # الواجهة الرئيسية (ترتيب عمودي)
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # تغيير خلفية التطبيق للون وردي لطيف جداً
        # Kivy يستخدم نظام الألوان النوافذ، سنقوم بتلوين العناصر بالداخل
        
        # 1. عنوان ترحيبي
        welcome_label = Label(
            text="✨ مـرحـبـاً بـكِ يـا جـمـيـلـة ✨\nأنا مساعدكِ الذكي لصنع أفكار تيك توك رهيبة! 💖",
            font_size='18sp',
            halign='center',
            color=get_color_from_hex('#FF69B4'), # لون وردي غامق للكتابة
            size_hint_y=None,
            height=80
        )
        main_layout.add_widget(welcome_label)
        
        # 2. خانة إدخال المجال أو الفكرة
        self.input_field = TextInput(
            hint_text="اكتبي هنا مجال قناتكِ (مثال: طبخ، دراسة، فيك)... 🌸👉🏻👈🏻",
            font_size='16sp',
            multiline=False,
            size_hint_y=None,
            height=50,
            background_color=get_color_from_hex('#FFF0F5'), # وردي فاتح جداً للهيكل
            foreground_color=get_color_from_hex('#4A4A4A')
        )
        main_layout.add_widget(self.input_field)
        
        # 3. زر التشغيل السحري
        generate_btn = Button(
            text="🎯 توليد أفكار إبداعية فوراً! 🌟",
            font_size='18sp',
            bold=True,
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=get_color_from_hex('#FF1493') # لون وردي فاقع وحيوي للزر
        )
        # ربط الزر بوظيفة توليد الأفكار عند الضغط
        generate_btn.bind(on_press=self.generate_ideas)
        main_layout.add_widget(generate_btn)
        
        # 4. منطقة عرض النتيجة (مع خاصية السكرول/التمرير للأعلى والأسفل إذا كانت الأفكار طويلة)
        scroll_view = ScrollView()
        self.result_label = Label(
            text="الأفكار السحرية ستظهر هنا... 🦄✨",
            font_size='16sp',
            color=get_color_from_hex('#333333'),
            halign='right',
            valign='top',
            size_hint_y=None
        )
        # جعل النص يتمدد تلقائياً حسب حجم الكلام
        self.result_label.bind(texture_size=self.result_label.setter('size'))
        
        scroll_view.add_widget(self.result_label)
        main_layout.add_widget(scroll_view)
        
        return main_layout

    def generate_ideas(self, instance):
        user_input = self.input_field.text.strip()
        
        if not user_input:
            self.result_label.text = "جميلتي، من فضلكِ اكتبي مجالاً أولاً لكي أساعدكِ! 🥺💞"
            return
            
        self.result_label.text = f"⏳ جاري التفكير بعمق وصنع أفكار خرافية لمجال ({user_input})..."
        
        # هنا يتم ربط الذكاء الاصطناعي مستقبلاً، حالياً سنضع ردوداً ذكية مجهزة ومزينة ومبهرة لص
