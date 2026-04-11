import datetime
from decimal import Decimal
import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.question import (
    question_1_query,
    question_2_query,
    question_3_query,
    question_4_query,
    question_5_query,
    question_6_query,
    question_7_query,
    question_8_query,
    question_9_query,
    question_10_query,
    question_11_query,
    question_12_query,
    question_13_query,
    question_14_query,
    question_15_query,
)


def run_common_test(expected_data, tested_func):
    result = tested_func()
    assert result == expected_data


# Q1: Yaşı 22'den büyük öğrencileri listele (tüm kolonlar)
def test_question_1_query():
    expected = [
        (2, 'Ayşe', 'Demir', 'ayse@example.com', 23),
        (4, 'Zeynep', 'Aydın', 'zeynep@example.com', 24),
    ]
    run_common_test(expected, question_1_query)


# Q2: Kurs kategorisi 'Veritabanı' olanları getir (tüm kolonlar)
def test_question_2_query():
    expected = [
        (1, 'SQL Temelleri', 'Veritabanı'),
        (2, 'İleri SQL', 'Veritabanı'),
    ]
    run_common_test(expected, question_2_query)


# Q3: İsmi 'A' harfi ile başlayan öğrencileri bul (tüm kolonlar)
def test_question_3_query():
    expected = [
        (1, 'Ahmet', 'Yılmaz', 'ahmet@example.com', 21),
        (2, 'Ayşe', 'Demir', 'ayse@example.com', 23),
    ]
    run_common_test(expected, question_3_query)


# Q4: Kurs ismi içinde 'SQL' geçenleri listele (tüm kolonlar)
def test_question_4_query():
    expected = [
        (1, 'SQL Temelleri', 'Veritabanı'),
        (2, 'İleri SQL', 'Veritabanı'),
    ]
    run_common_test(expected, question_4_query)


# Q5: Yaşı 22 ile 24 arasında olan öğrencileri getir (tüm kolonlar)
def test_question_5_query():
    expected = [
        (2, 'Ayşe', 'Demir', 'ayse@example.com', 23),
        (3, 'Mehmet', 'Kaya', 'mehmet@example.com', 22),
        (4, 'Zeynep', 'Aydın', 'zeynep@example.com', 24),
    ]
    run_common_test(expected, question_5_query)


# Q6: Kursa kayıtlı olan öğrencilerin isimlerini listele (first_name, last_name — DISTINCT)
def test_question_6_query():
    expected = {
        ('Ahmet', 'Yılmaz'),
        ('Ayşe', 'Demir'),
        ('Mehmet', 'Kaya'),
        ('Zeynep', 'Aydın'),
    }
    result = question_6_query()
    assert set(result) == expected


# Q7: Veritabanı kategorisindeki kurslara kayıtlı öğrenci sayısını bul (course_name, student_count)
def test_question_7_query():
    expected = {
        ('SQL Temelleri', 2),
        ('İleri SQL', 1),
    }
    result = question_7_query()
    assert set(result) == expected


# Q8: Her kursun adını ve bu kursu veren öğretmenin adını getir (course_name, instructor_name)
def test_question_8_query():
    expected = [
        ('SQL Temelleri', 'Ali Hoca'),
        ('İleri SQL', 'Ali Hoca'),
        ('JavaScript 101', 'Elif Hoca'),
        ('Python Giriş', 'Murat Hoca'),
    ]
    run_common_test(expected, question_8_query)


# Q9: Kayıtlı olmayan öğrencileri listele (tüm kolonlar)
def test_question_9_query():
    expected = [
        (5, 'Can', 'Öztürk', 'can@example.com', 20),
    ]
    run_common_test(expected, question_9_query)


# Q10: Kurslara göre ortalama öğrenci yaşı (course_name, avg_age)
def test_question_10_query():
    result = question_10_query()
    avg_ages = {r[0]: r[1] for r in result}
    assert avg_ages['SQL Temelleri'] == Decimal('22.0000000000000000')
    assert avg_ages['İleri SQL'] == Decimal('21.0000000000000000')
    assert avg_ages['JavaScript 101'] == Decimal('22.0000000000000000')
    assert avg_ages['Python Giriş'] == Decimal('24.0000000000000000')


# Q11: Öğrenci başına toplam kayıtlı kurs sayısı (first_name, last_name, total_courses)
def test_question_11_query():
    result = question_11_query()
    counts = {(r[0], r[1]): r[2] for r in result}
    assert counts[('Ahmet', 'Yılmaz')] == 2
    assert counts[('Ayşe', 'Demir')] == 1
    assert counts[('Mehmet', 'Kaya')] == 1
    assert counts[('Zeynep', 'Aydın')] == 1


# Q12: Birden fazla kurs veren öğretmenler (instructor_name, total_courses)
def test_question_12_query():
    expected = [
        ('Ali Hoca', 2),
    ]
    run_common_test(expected, question_12_query)


# Q13: Kurslara göre kaç farklı öğrenci kayıtlı (course_name, unique_students)
def test_question_13_query():
    result = question_13_query()
    counts = {r[0]: r[1] for r in result}
    assert counts['SQL Temelleri'] == 2
    assert counts['İleri SQL'] == 1
    assert counts['JavaScript 101'] == 1
    assert counts['Python Giriş'] == 1


# Q14: Hem 'SQL Temelleri' hem 'İleri SQL' kursuna kayıtlı öğrenciler (first_name, last_name)
def test_question_14_query():
    expected = [
        ('Ahmet', 'Yılmaz'),
    ]
    run_common_test(expected, question_14_query)


# Q15: Kurs, öğretmen, öğrenci ve kayıt tarihlerini birleştir
def test_question_15_query():
    expected = [
        ('Ahmet', 'Yılmaz', 'SQL Temelleri', 'Ali Hoca', datetime.date(2023, 10, 1)),
        ('Ahmet', 'Yılmaz', 'İleri SQL', 'Ali Hoca', datetime.date(2023, 11, 15)),
        ('Ayşe', 'Demir', 'SQL Temelleri', 'Ali Hoca', datetime.date(2023, 10, 1)),
        ('Mehmet', 'Kaya', 'JavaScript 101', 'Elif Hoca', datetime.date(2023, 9, 20)),
        ('Zeynep', 'Aydın', 'Python Giriş', 'Murat Hoca', datetime.date(2023, 8, 15)),
    ]
    run_common_test(expected, question_15_query)


def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")


class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1


def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    total = collector.passed + collector.failed
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")

    if total == 0:
        print("Hiç test çalıştırılmadı.")
        return

    user_score = round((collector.passed / total) * 100, 2)
    print(f"Skor: {user_score}")

    url = "https://kaizu-api-8cd10af40cb3.herokuapp.com/projectLog"
    payload = {
        "user_id": 506,
        "project_id": 35,
        "user_score": user_score,
        "is_auto": False
    }
    headers = {"Content-Type": "application/json"}
    send_post_request(url, payload, headers)


if __name__ == "__main__":
    run_tests()
