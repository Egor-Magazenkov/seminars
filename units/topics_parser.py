import pandas as pd
from jinja2 import Environment, FileSystemLoader

def csv_to_html(csv_path):
    df = pd.read_csv(csv_path)

    safe_columns = [
        'Тема доклада', 
        'Фамилия Имя', 
        'Краткая информация о себе', 
        'Формат доклада (может подходить под несколько)', 
        'Краткая аннотация', 
        'Пререквизиты', 
        'Краткое содержание доклада = основные рассматриваемые пункты, понятия, результаты '
    ]
    safe_df = df[safe_columns]

    # 3. Clean the data: replace empty cells (NaN) with empty strings
    safe_df = safe_df.fillna("")

    # Convert dataframe to a list of dictionaries
    seminars_data = safe_df.to_dict(orient='records')

    # 4. Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('../assets/'))
    template = env.get_template('unit_template.jinja')

    # 5. Render and print HTML to Quarto
    print(template.render(seminars=seminars_data))
