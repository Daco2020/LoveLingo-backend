import abc

from app.models import LoveLingo, LoveLingoChoice


love_lingo_table: list[LoveLingo] = [
    LoveLingo(
        id=1,
        type="A",
        name="인정하는 말",
        description="인정하는말(상대에 대한 칭찬과 격려) 다른 사람을 인정하는 말로 사랑을 표현하는 것입니다. 상대방의 성격이나 외모 또는 그가 당신이나 다른 사람들을 위해 한 일에 초점을 맞춘 말일 수도 있습니다. 이 언어로 말하려면 감사하거나 존중할 만한 면을 상대에게서 살핀 후 그것을 말로 표현하는 것 입니다.",  # noqa: E501
    ),
    LoveLingo(
        id=2,
        type="B",
        name="함께하는 시간",
        description="함께하는 시간 (진정한 대화, 취미 활동) 이는 상대방에게 집중하는 시간을 가리킵니다. TV를 끄고, 탁자에 놓인 잡지도 치우고, 서로를 바라보며 대화하는 것입니다. 운동을 위해거사 아니가 함께하는 시간을 갖기 위해 산책할 수도 있습니다. 다른 어떤 것보다 함께하는 시간을 가질 때 사랑받는다고 느끼는 사람들이 있습니다.",  # noqa: E501
    ),
    LoveLingo(
        id=3,
        type="C",
        name="선물",
        description="선물 (가장 배우기 쉬운 사랑의 언어) 어떤 사람들은 선물을 받을 때 자신이 사랑받고 있음을 가장 많이 느낍니다. 선물을 받으면 '나를 무척 생각하고 있구나' 라고 생각합니다. 최상의 선물은 상대방이 고맙게 여길 만한 것입니다. 선물이 꼭 비싸야 하는것은 절대 아니죠. 장미 한송이, 막대사탕, 엽서, 한 권의 책 등으로도 사랑을 깊이 있게 전할 수있습니다.",  # noqa: E501
    ),
    LoveLingo(
        id=4,
        type="D",
        name="봉사",
        description="봉사 (원하는 것을 몸으로 봉사해주기) 이런 사함들에게는 말보다 행동이 더 중요합니다. 만일 당신이 그들에게 '당신은 대단해요', '고마워요', '사랑해요'라며 인정하는 말을 하면 그들은 '당신이 나를 사랑한다면 집안일을 좀 도와주는 게 어떻겠어요?'하고 생각할 것입니다. 만일 봉사가 그들의 주된 사랑의 언어라면 그들을 사랑하는 비결은 그들이 해주기를 바라는 일을 찾아내고, 그 일을 꾸준히 하는 것입니다.",  # noqa: E501
    ),
    LoveLingo(
        id=5,
        type="E",
        name="스킨십",
        description="스킨십 (육체적 접촉을 통한 교감 증대) 스킨십의 정서적인 힘에 대해서는 대부분 잘 알고 있을 것입니다. 연구에 의하면, 오랫동안 스킨십을 하지 않은 아기들 보단 껴안거나 어루만지는 손길을 많이 받은 아기들이 정서적으로 더 양호합니다. 스킨십이 주된 사랑의 언어인 사람에게는 적절한 접촉이 가장 깊이 있는 사랑 표현 방법입니다.",  # noqa: E501
    ),
]

choice_table = [
    LoveLingoChoice(
        content='요리를 만들었을 때 상대방이 "너의 요리 솜씨가 정말 훌륭해, 맛있어"라고 칭찬하기', love_lingo_id=1
    ),
    LoveLingoChoice(
        content='새로운 옷을 입었을 때 상대방이 "그 옷이 너에게 정말 잘 어울려, 멋져"라고 칭찬하기', love_lingo_id=1
    ),
    LoveLingoChoice(
        content='시험에서 좋은 성적을 받았을 때 상대방이 "너는 정말 똑똑하고 열심히 공부하는구나"라고 칭찬하기',
        love_lingo_id=1,
    ),
    LoveLingoChoice(
        content='자기 작품을 완성했을 때 상대방이 "이 작품은 정말 완벽해, 대단하다"라고 칭찬하기', love_lingo_id=1
    ),
    LoveLingoChoice(
        content='프로젝트를 완료했을 때 상대방이 "너의 노력이 이 프로젝트를 성공으로 이끌었어, 대단해"라고 칭찬하기',
        love_lingo_id=1,
    ),
    LoveLingoChoice(
        content='힘든 일을 견뎌낼 때 상대방이 "너의 인내심과 용기에 박수를 보냅니다"라고 격려하기', love_lingo_id=1
    ),
    LoveLingoChoice(content="내가 힘든 시기에 상대방이 함께 걷기를 제안하며 위로를 받기", love_lingo_id=2),
    LoveLingoChoice(content="내가 요리에 관심을 가지고 있을 때 상대방이 함께 요리를 해주기", love_lingo_id=2),
    LoveLingoChoice(content="내가 스트레스를 받을 때 상대방이 영화나 공연을 보자고 제안하기", love_lingo_id=2),
    LoveLingoChoice(content="내가 좋아하는 작가의 책 발표회에 상대방이 함께 참석해주기", love_lingo_id=2),
    LoveLingoChoice(content="내가 우울한 날에 상대방이 함께 공원에서 피크닉을 즐기자고 제안하기", love_lingo_id=2),
    LoveLingoChoice(content="내가 새로운 취미를 찾고자 할 때 상대방이 함께 도전해주기", love_lingo_id=2),
    LoveLingoChoice(content="내가 취업에 성공하거나 승진할 때 상대방이 축하 선물을 준비해주기", love_lingo_id=3),
    LoveLingoChoice(content="내가 감기에 걸릴 때 상대방이 직접 끓여준 수프를 받기", love_lingo_id=3),
    LoveLingoChoice(content="내가 필요한 물건을 상대방이 사다 주기", love_lingo_id=3),
    LoveLingoChoice(content="내 생일에 상대방이 나를 위해 특별한 선물을 준비해주기", love_lingo_id=3),
    LoveLingoChoice(content="내가 좋아하는 뮤지션의 콘서트 티켓을 받기", love_lingo_id=3),
    LoveLingoChoice(content="내가 기분이 좋지 않을 때 상대방이 좋아하는 디저트를 받기", love_lingo_id=3),
    LoveLingoChoice(content="내가 업무에 지칠 때 상대방이 위로와 격려의 말을 건네주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 힘들어할 때 상대방이 집안일을 도와주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 아플 때 상대방이 간호해주며 걱정해주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 바쁜 기간 동안 상대방이 나를 위해 요리를 만들어주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 급한 일이 생겼을 때 상대방이 도움을 주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 힘든 시기에 상대방이 나를 격려하고 함께 문제를 해결해주기", love_lingo_id=4),
    LoveLingoChoice(content="내가 힘든 날 상대방이 위로의 말과 함께 뒤에서 포옹해주기", love_lingo_id=5),
    LoveLingoChoice(content="내가 피곤한 상태일 때 상대방이 발마사지를 해주기", love_lingo_id=5),
    LoveLingoChoice(
        content="내가 속상한 마음을 털어놓았을 때 상대방이 손을 잡아주며 이야기 들어주기", love_lingo_id=5
    ),
    LoveLingoChoice(content="내가 추운 날씨에 상대방이 옷깃을 걷어주고 나를 따뜻하게 감싸주기", love_lingo_id=5),
    LoveLingoChoice(
        content="내가 긴장한 상태일 때 상대방이 손목에 가볍게 손을 대고 안정을 주는 말을 건네주기", love_lingo_id=5
    ),
    LoveLingoChoice(content="내가 스트레스를 받을 때 상대방이 어깨에 팔을 얹으며 응원의 말 전하기", love_lingo_id=5),
]


class LoveLingoRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch(self) -> list[LoveLingoChoice]:
        ...


class MemoryLoveLingoRepository(LoveLingoRepository):
    def __init__(
        self,
        love_lingo_table: list[LoveLingo],
        choice_table: list[LoveLingoChoice],
    ) -> None:
        self._love_lingo_table = love_lingo_table
        self._choice_table = choice_table

    async def fetch(self) -> list[LoveLingoChoice]:
        return self._choice_table
