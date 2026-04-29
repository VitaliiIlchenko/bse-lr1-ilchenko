# Лабораторна робота №2: Проектування архітектури ПЗ
**Студент:** Ільченко Віталій  
**Проєкт:** SmartDoc AI (Система розпізнавання документів)

## 1. Функціональні вимоги (FR)
| ID | Опис вимоги |
|:---|:---|
| FR-01 | Користувач повинен мати можливість завантажувати файли форматів PDF, JPG, PNG до 20МБ. |
| FR-02 | Система повинна автоматично розпізнавати суми та дати за допомогою ШІ. |
| FR-03 | Користувач повинен мати можливість редагувати витягнуті дані перед збереженням. |
| FR-04 | Система повинна зберігати історію оброблених документів у профілі користувача. |
| FR-05 | Адміністратор повинен мати можливість переглядати статистику використання системи. |

## 2. Діаграма прецедентів-дій (Use Case)

```mermaid
graph TD
    User((Користувач))
    Admin((Адміністратор))
    AI_Service[AI Service System]

    User --- UC1[Завантажити документ]
    User --- UC2[Редагувати дані]
    User --- UC3[Переглянути історію]
    
    UC1 -.-> UC4[AI розпізнавання]
    UC4 --- AI_Service
    
    Admin --- UC5[Керувати лімітами]
    Admin --- UC6[Переглянути статистику]
```
## 3. Діаграма класів (Class Diagram)

```mermaid
classDiagram
    class User {
        +int id
        +string name
        +uploadDocument(file)
    }
    class Document {
        +int id
        +string filename
        +float size
        +status state
    }
    class OCR Engine {
        +process(file)
        +validateFormat()
    }
    class DataReport {
        +date document_date
        +float amount
        +saveChanges()
    }
    class Database {
        +saveRecord()
        +fetchHistory()
    }

    User "1" -- "*" Document : завантажує
    Document "1" -- "1" OCREngine : обробляється
    OCREngine "1" -- "1" DataReport : генерує
    DataReport "*" -- "1" Database : зберігається
```
## 4. Діаграма послідовності (Sequence Diagram)

```mermaid
sequenceDiagram
    participant U as Користувач
    participant S as Система/UI
    participant AI as Optical Character Recognition Engine (AI)
    participant DB as База даних

    U->>S: Завантажити файл (invoice.pdf)
    S->>S: Перевірка формату та розміру
    S->>AI: Надіслати файл на розпізнавання
    AI-->>S: Повернути суму та дату
    S->>U: Показати розпізнані дані
    U->>S: Натиснути "Зберегти"
    S->>DB: Записати дані в історію
    DB-->>S: Підтверджено
    S-->>U: Успішно збережено
```
## 5. Матриця трасованості-зв'язок (Traceability)
| FR ID | Назва вимоги | Прецедент | Класи | Діаграма послідовності |
|:---|:---|:---|:---|:---|
| FR-01 | Завантаження документів | Завантажити документ | User, Document | Сценарій завантаження |
| FR-02 | AI розпізнавання | AI розпізнавання | OCREngine | Сценарій обробки AI |
| FR-03 | Редагування даних | Редагувати дані | DataReport | Сценарій збереження |
| FR-04 | Зберігання історії | Переглянути історію | Database | - |
| FR-05 | Статистика системи | Переглянути статистику | User (Admin) | - |
