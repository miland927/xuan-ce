from __future__ import annotations

import random
from datetime import date


TG = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
DZ = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

GUA_DATA = [
    {"n": "乾为天", "short": "乾", "serial": "01", "verdict": "大吉", "keyword": "刚健进取，宜主动开局。", "lines": [1, 1, 1, 1, 1, 1], "guaci": "乾，元亨利贞。象曰：天行健，君子以自强不息。", "jiedu": "纯阳刚健，万象之始。此卦主进取，宜大胆开创，守正而行，万事可成。", "story": "相传周文王被囚羑里，演六十四卦时首列乾卦。乾者，天也。古人观天象，见日月星辰运行不息，感悟天行健，君子以自强不息，将此精神融入乾卦之中。历代君王即位，必问乾卦，取其刚健之意，自勉奋进。", "yao_key": "潜龙勿用→见龙在田→终日乾乾→或跃在渊→飞龙在天→亢龙有悔"},
    {"n": "坤为地", "short": "坤", "serial": "02", "verdict": "中吉", "keyword": "厚德载物，宜承接与积累。", "lines": [0, 0, 0, 0, 0, 0], "guaci": "坤，元亨，利牝马之贞。象曰：地势坤，君子以厚德载物。", "jiedu": "纯阴柔顺，大地之象。宜顺势而为，不可强行争先，以柔克刚，积累实力。", "story": "坤卦六爻皆阴，象征大地包容万物。古人感悟大地承载山川、滋养万物而不居功，创出坤卦。", "yao_key": "履霜坚冰至→直方大→含章可贞→括囊无咎→黄裳元吉→龙战于野"},
    {"n": "水雷屯", "short": "屯", "serial": "03", "verdict": "小吉", "keyword": "初生之难，宜守正待时。", "lines": [1, 0, 0, 0, 1, 0], "guaci": "屯，元亨利贞，勿用有攸往，利建侯。象曰：云雷，屯；君子以经纶。", "jiedu": "草木初萌，破土艰难。万事开头难，此时宜守正待时，广结援助，不可冒进。", "story": "屯字象形，如草木初生破土之状。卦取云雷，雷震于云中，蓄势而未发。", "yao_key": "磐桓→屯如邅如→即鹿无虞→乘马班如→屯其膏→乘马班如泣血"},
    {"n": "山水蒙", "short": "蒙", "serial": "04", "verdict": "平", "keyword": "事有迷雾，宜求证再动。", "lines": [0, 1, 0, 0, 0, 1], "guaci": "蒙，亨。匪我求童蒙，童蒙求我。象曰：山下出泉，蒙；君子以果行育德。", "jiedu": "山下泉水，蒙昧初开。此卦主教化与启蒙，宜虚心求教，明辨是非，不可固执己见。", "story": "蒙卦讲述一段师生问答。山下出泉，泉水不择路，遇石则绕，遇土则渗，终汇成江河。", "yao_key": "发蒙→包蒙→勿用取女→困蒙→童蒙吉→击蒙"},
    {"n": "水天需", "short": "需", "serial": "05", "verdict": "吉", "keyword": "等待时机，守正可成。", "lines": [1, 0, 0, 1, 1, 1], "guaci": "需，有孚，光亨，贞吉，利涉大川。象曰：云上于天，需；君子以饮食宴乐。", "jiedu": "云气聚天，雨将至而未至。此卦主等待，时机未熟，宜养精蓄锐，切勿强行出击。", "story": "云在天上聚而未降，正是积蓄能量之时。等待不是消极，而是以退为进，蓄势待发的智慧。", "yao_key": "需于郊→需于沙→需于泥→需于血→需于酒食→入于穴"},
    {"n": "天水讼", "short": "讼", "serial": "06", "verdict": "小凶", "keyword": "易有争执，宜退一步。", "lines": [1, 1, 1, 0, 0, 1], "guaci": "讼，有孚，窒惕，中吉，终凶。利见大人，不利涉大川。象曰：天与水违行，讼；君子以作事谋始。", "jiedu": "天水相违，争讼之象。此卦主纷争，宜和解退让，若坚持到底终必有失。", "story": "讼卦提醒：争讼之前先问动机，若能和解，莫逞一时之气。", "yao_key": "不永所事→不克讼→食旧德→不克讼→讼元吉→或锡之鞶带"},
    {"n": "地水师", "short": "师", "serial": "07", "verdict": "中吉", "keyword": "组织协力，先定规则。", "lines": [0, 0, 0, 0, 1, 0], "guaci": "师，贞，丈人，吉无咎。象曰：地中有水，师；君子以容民畜众。", "jiedu": "地中蓄水，众兵之象。此卦主团队与统领，宜建立秩序、明确规则，以德服众。", "story": "师卦之义，是凝聚人心、建立信任、运营团队的大智慧。", "yao_key": "师出以律→在师中→师或舆尸→师左次→田有禽→大君有命"},
    {"n": "水地比", "short": "比", "serial": "08", "verdict": "吉", "keyword": "亲比之象，结交善友。", "lines": [0, 1, 0, 0, 0, 0], "guaci": "比，吉。原筮，元永贞，无咎。象曰：地上有水，比；先王以建万国，亲诸侯。", "jiedu": "地上有水，相亲相近。此卦主联合与亲附，宜广结善缘，寻找志同道合之人。", "story": "比卦告诉我们：人生需要盟友，善于结交真诚之人，彼此扶持，方能走得更远。", "yao_key": "有孚比之→比之自内→比之匪人→外比之→显比→比之无首"},
]

YI_POOL = ["出行", "签约", "会友", "祈福", "开业", "搬迁", "嫁娶", "求医", "纳财", "动土", "装修", "求职", "读书", "健身"]
JI_POOL = ["诉讼", "动土", "大事", "远行", "借贷", "置产", "开刀", "赴宴", "争执", "冒险", "熬夜", "铺张"]
DIR_POOL = ["正东", "正南", "正西", "正北", "东南", "东北", "西南", "西北"]


def calc_bazi(year: int, month: int, day: int, hour: int) -> dict:
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    hour_idx = ((hour + 1) % 24) // 2

    year_tg = TG[(year - 4) % 10]
    year_dz = DZ[(year - 4) % 12]
    month_tg = TG[(((year - 4) % 5) * 2 + month - 1) % 10]
    month_dz = DZ[(month + 1) % 12]
    day_base = (year * 365 + year // 4 + day + month * 30 + 15) % 60
    day_tg = TG[day_base % 10]
    day_dz = DZ[day_base % 12]
    hour_tg = TG[((day_base % 5) * 2 + (hour_idx % 2)) % 10]
    hour_dz = DZ[hour_idx % 12]

    tian = [year_tg, month_tg, day_tg, hour_tg]
    di = [year_dz, month_dz, day_dz, hour_dz]
    joined = "".join(tian + di)
    wuxing = {
        "木": sum(joined.count(c) for c in "甲乙寅卯"),
        "火": sum(joined.count(c) for c in "丙丁巳午"),
        "土": sum(joined.count(c) for c in "戊己辰戌丑未"),
        "金": sum(joined.count(c) for c in "庚辛申酉"),
        "水": sum(joined.count(c) for c in "壬癸亥子"),
    }
    max_count = max(wuxing.values())
    min_count = min(wuxing.values())
    strong = "、".join(k for k, v in wuxing.items() if v == max_count)
    weak = "、".join(k for k, v in wuxing.items() if v == min_count)
    summary = (
        f"年柱{year_tg}{year_dz}，月柱{month_tg}{month_dz}，"
        f"日柱{day_tg}{day_dz}，时柱{hour_tg}{hour_dz}。"
        f"日主为{day_tg}。{strong}偏旺，{weak}不足。"
    )
    return {"tian": tian, "di": di, "wuxing": wuxing, "strong": strong, "weak": weak, "summary": summary}


def _normalize_gua(item: dict) -> dict:
    result = dict(item)
    result["name"] = result.pop("n")
    return result


def cast_gua(method: str = "random") -> dict:
    rng = random.SystemRandom()
    gua = rng.choice(GUA_DATA)
    result = _normalize_gua(gua)
    result["lines"] = gua["lines"]
    result["method"] = method
    return result


def get_daily_gua() -> dict:
    rng = random.Random(date.today().toordinal())
    result = _normalize_gua(rng.choice(GUA_DATA))
    result["lines"] = result["lines"]
    result["method"] = "daily"
    result["yi"] = rng.sample(YI_POOL, 3)
    result["ji"] = rng.sample(JI_POOL, 3)
    result["lucky_dirs"] = rng.sample(DIR_POOL, 3)
    result["minsuo"] = f"今日黄历：宜{result['yi'][0]}、{result['yi'][1]}、{result['yi'][2]}；忌{result['ji'][0]}、{result['ji'][1]}、{result['ji'][2]}。"
    return result
