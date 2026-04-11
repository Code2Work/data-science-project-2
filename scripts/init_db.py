import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="1234"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INT
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    category VARCHAR(50)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    expertise VARCHAR(100)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    enrollment_date DATE
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS course_instructors (
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(course_id),
    instructor_id INT REFERENCES instructors(instructor_id)
);
""")

cur.execute("""
INSERT INTO students (first_name, last_name, email, age) VALUES
('Ahmet', 'Yılmaz', 'ahmet@example.com', 21),
('Ayşe', 'Demir', 'ayse@example.com', 23),
('Mehmet', 'Kaya', 'mehmet@example.com', 22),
('Zeynep', 'Aydın', 'zeynep@example.com', 24),
('Can', 'Öztürk', 'can@example.com', 20);
""")

cur.execute("""
INSERT INTO courses (course_name, category) VALUES
('SQL Temelleri', 'Veritabanı'),
('İleri SQL', 'Veritabanı'),
('JavaScript 101', 'Programlama'),
('Python Giriş', 'Programlama');
""")

cur.execute("""
INSERT INTO instructors (name, expertise) VALUES
('Ali Hoca', 'Veritabanı'),
('Elif Hoca', 'Frontend'),
('Murat Hoca', 'Backend');
""")

cur.execute("""
INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2023-10-01'),
(1, 2, '2023-11-15'),
(2, 1, '2023-10-01'),
(3, 3, '2023-09-20'),
(4, 4, '2023-08-15');
""")

cur.execute("""
INSERT INTO course_instructors (course_id, instructor_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3);
""")

conn.commit()
cur.close()
conn.close()
