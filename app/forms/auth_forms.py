from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistroForm(FlaskForm):
    nome = StringField(
        "Nome Completo", validators=[DataRequired(message="O nome é obrigatório.")]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="O e-mail é obrigatório."),
            Email(message="Digite um endereço de e-mail válido."),
        ],
    )
    senha = PasswordField(
        "Senha",
        validators=[
            DataRequired(),
            Length(min=6, message="A senha deve ter pelo menos 6 caracteres."),
        ],
    )
    confirmacao_senha = PasswordField(
        "Confirmar Senha",
        validators=[
            DataRequired(),
            EqualTo("senha", message="As senhas não coincidem. Tente novamente."),
        ],
    )
    submit = SubmitField("Finalizar Cadastro")

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(message="O e-mail é obrigatório."),
        Email(message="Digite um e-mail válido.")
    ])
    
    senha = PasswordField('Senha', validators=[
        DataRequired(message="A senha é obrigatória.")
    ])
    
    submit = SubmitField('Entrar no Sistema')