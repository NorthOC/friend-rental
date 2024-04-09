from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

class CityOfService(models.TextChoices):
    """ List of Lithuanian cities """
    VILNIUS = "Vilnius"
    KAUNAS = "Kaunas"
    KLAIPEDA = "Klaipėda"
    SIAULIAI = "Šiauliai"
    PANEVEZYS = "Panevėžys"
    AKMENE = "Akmenė"
    ALYTUS = "Alytus"
    ANYKSCIAI = "Anykščiai"
    BIRSTONAS = "Birštonas"
    BIRZAI = "Biržai"
    DRUSKININKAI = "Druskininkai"
    ELEKTRENAI = "Elektrėnai"
    GARGZDAI = "Gargždai"
    IGNALINA = "Ignalina"
    JONAVA = "Jonava"
    JONISKIS = "Joniškis"
    JURBARKAS = "Jurbarkas"
    KAISIADORYS = "Kaišiadorys"
    KALVARIJA = "Kalvarija"
    KAZLU_RUDA = "Kazlų Rūda"
    KEDAINIAI = "Kėdainiai"
    KELME = "Kelmė"
    KREKENAVA = "Krekenava"
    KRETINGA = "Kretinga"
    KUPISKIS = "Kupiškis"
    KURSENAI = "Kuršėnai"
    LAZDIJAI = "Lazdijai"
    LENTVARIS = "Lentvaris"
    MARIJAMPOLE = "Marijampolė"
    MAZEIKIAI = "Mažeikiai"
    MOLETAI = "Molėtai"
    NAUJOJI_AKMENE = "Naujoji Akmenė"
    NEMENCINE = "Nemenčinė"
    NERINGA = "Neringa"
    PABRADE = "Pabradė"
    PAGEGIAI = "Pagėgiai"
    PAKRUOJIS = "Pakruojis"
    PALANGA = "Palanga"
    PASVALYS = "Pasvalys"
    PLUNGE = "Plungė"
    PRIENAI = "Prienai"
    RADVILISKIS = "Radviliškis"
    RASEINIAI = "Raseiniai"
    RIETAVAS = "Rietavas"
    ROKISKIS = "Rokiškis"
    SAKIAI = "Šakiai"
    SALCININKAI = "Šalčininkai"
    SILALE = "Šilalė"
    SILUTE = "Šilutė"
    SIRVINTOS = "Širvintos"
    SKUODAS = "Skuodas"
    SVENCIONYS = "Švenčionys"
    TAURAGE = "Tauragė"
    TELSIAI = "Telšiai"
    TRAKAI = "Trakai"
    UKMERGE = "Ukmergė"
    UTENA = "Utena"
    VARENA = "Varėna"
    VIEVIS = "Vievis"
    VILKAVISKIS = "Vilkaviškis"
    VISAGINAS = "Visaginas"
    ZARASAI = "Zarasai"
    NUOTOLINIU = "Nuotoliniu"

class Gender(models.TextChoices):
    VYR = "vyr"
    MOT = "mot"

class User(AbstractUser):
    """
    User model
    ________________
    +email
    +password
    +is_activated - used for email activation
    +is_id_verified - use for id verification
    +profile_type - determines if user or friend

    +wallet - virtual wallet

    +first_name
    +last_name
    +birthday
    +city - choice where service is provided (remote opt included)
    +education_level - vidurinis, auštasis, aukštesnysis, kitas
    +job
    +description
    +personality_type - 16 types
    +sex - vyr, mot
    +height_cm

    link_one - url to their website
    link_two - url to their website
    link_one_name
    link_two_name
    img_one     --
    img_two      |______ images
    img_three   --
    interest_one    --
    interest_two     |_____ interests
    interest_three   |
    interest_four   --
    interest_color_one      --
    interest_color_two       |_____ interest box bg color
    interest_color_three     |
    interest_color_four     --
    """

    class ProfileTypes(models.TextChoices):
        # users have a different profile type from friends
        USER = "USER", _("User")
        FRIEND = "FRIEND", _("Friend")
    
    class EducationLevels(models.TextChoices):
        VIDURINIS = "Vidurinis"
        AUKSTESNYSIS = "Aukštesnysis"
        AUKSTASIS = "AUKŠTASIS"
    
    class PersonalityTypes(models.TextChoices):
        #purple
        INTJ = "INTJ"
        INTP = "INTP"
        ENTJ = "ENTJ"
        ENTP = "ENTP"

        #green
        INFJ = "INFJ"
        INFP = "INFP"
        ENFJ = "ENFJ"
        ENFP = "ENFP"

        #blue
        ISTJ = "ISTJ"
        ISFJ = "ISFJ"
        ESTJ = "ESTJ"
        ESFJ = "ESFJ"

        #yellow
        ISTP = "ISTP"
        ISFP = "ISFP"
        ESTP = "ESTP"
        ESFP = "ESFP"

    # for login (using email)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_activated = models.BooleanField(default=False)
    is_id_verified = models.BooleanField(default=False)

    profile_type = models.CharField(max_length=6, 
                                    choices=ProfileTypes, 
                                    default=ProfileTypes.USER)
    wallet = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=15,
                            choices=CityOfService,
                            null=True,
                            blank=True)
    job = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    personality_type = models.CharField(max_length=4,
                                        choices=PersonalityTypes,
                                        null=True,
                                        blank=True)
    sex = models.CharField(max_length=3, blank=True, null=True)
    height_cm = models.PositiveIntegerField(blank=True, 
                                            null=True, 
                                            validators=[MinValueValidator(0), MaxValueValidator(300)])
