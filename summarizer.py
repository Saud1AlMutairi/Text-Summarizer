import os
from google import genai
from google.genai import errors

# إعداد مفتاح الـ API (تأكد من حفظ المفتاح كمتض بيئة أو وضعه مباشرة هنا للاختبار)
# يمكنك الحصول على المفتاح مجاناً من Google AI Studio
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def summarize_text(text: str, max_words: int = 100) -> str:
    """
    تقوم هذه الدالة بتلخيص النص المدخل باستخدام نموذج Gemini
    """
    prompt = f"""
    قم بتلخيص النص التالي بدقة واحترافية، مع الاحتفاظ بالأفكار الرئيسية والمهمة فقط.
    اجعل التلخيص في حدود {max_words} كلمة تقريباً.
    
    النص المراد تلخيصه:
    {text}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except errors.APIError as e:
        return f"حدث خطأ أثناء الاتصال بخدمة الذكاء الاصطناعي: {e}"

if __name__ == "__main__":
    # نص تجريبي للتجربة
    sample_text = """
    الذكاء الاصطناعي (Artificial Intelligence) هو فرع من علوم الحاسوب يهدف إلى إنشاء أنظمة قادرة على محاكاة القدرات الذكية للبشر، 
    مثل التعلم، والاستنتاج، وحل المشكلات، وفهم اللغة الطبيعية. يشهد هذا المجال تطوراً هائلاً في الآونة الأخيرة بفضل توافر كميات هائلة من البيانات 
    وقوة الحوسبة العالية، مما أدى إلى دخول تطبيقاته في شتى مناحي الحياة مثل الرعاية الصحية، والتعليم، والنقل، والصناعة، وتطوير البرمجيات.
    """
    
    print("--- النص الأصلي ---")
    print(sample_text)
    
    print("\n--- جاري التلخيص... ---")
    summary = summarize_text(sample_text, max_words=40)
    
    print("\n--- النتيجة ---")
    print(summary)
