#coding:L1
import zlib,hashlib
b=bytes("""xœÝXÍn7¾û)¶¾DƒäCÒ@}ŽÄ(æ×êÈ†ì´Eƒ¼{gmÉ½{0²ír9Ão¾ùÕ^¿<ÜŸŸ–=îŽ|ñúx¶‹ÃòqùôÎ€ç ª™réZY\r­BpD¦Ò«'ãnœ¥'“šk*ìX:¨Žwï—wD4c\r±z¦š½Æv–VdÎ	Æˆdˆ˜ÊlÃÕ‰Ê\0îÙ°*ç«µ®™{	–
wñTM½%(2LÜiú¤4ê,¹žã´FÝ:6í«ŽTz= ·^X•FÊœ]´I*- ä,¡-t	ø,M“…6#óG±Bê=÷Î¹*K.šªx£g¤’)C©'ÊXSrÆ°ÍV[p
Þ'sç
Sƒ’±e%s…VÁ‘U•Ø,–@ç1„RE5Zu”à´Hš-u²[Å7h8F£0JxEKÍ0ëœ=ö„A›¹àf¾Ý€Ó_)>»MhÖ“„c¥¹ô&–4	Ÿƒ[-ÅRÌ%%Aíž=nIq+[¶ˆ±<HÀ:Tð”qÌ$-§°ÎÃÀ‚9ãÔià\r[¬eHNž&T¯>¬nÅiiÅs’Ç³„DjS“ÒšñÊjc«šµ³8©½ÔA£èôœóª›„á¹j™‘Ùç×uÖÈ)áHPƒI“´FÊdNCbKÑ²ê¨agÞóÔÊìyf#Í`%+(·. 6›€U'VÅ¹äà(²1oÅ‡hŠÌ\rsíŒÒ¸ºGÒ¨›5¤'‚ Òœæ™Ã¢JbZ\0d’[™[ñAB2P’ašB3ÂiMÞdEID8 EŠ,Ùƒ6±¨3#"2b=måÛ-êGæŒœCGa×5©º)óhBÔSKZQr"Ò“²‘|ÀÀ®<·òË&ñA³œK°É¬BNR 3L* ½«4÷0¥ZT˜jzt\0Z£*mÕçÞJ¿Ý¢ÏmQO¥ÜßBÇ¶lQƒÞŠo·˜é¶ðË}ÿ­púVòåÍôÊ7§[Ôä-ú‰³:5ÕudÏÃÅ1DÔj\râ¼h9-Â½‡ð¨Ä&bMíeN®CmÆC§äOk(:cB§Öjt¢>j'ç´†Z.Ne’tU‚…­f˜Mrƒ9h‹ÿ/oå»ÃÿöíÍ…ßÑíòq9ž¾>í.íôdçe]»^.÷WOçãÃnqôåt¿~»¹ò¯ww_èI»óåïwQ8>ûDþýãæâ÷Ïß/ß?Kï¯—‡óñ§¿èî¨‹ßŸCn¹Þ]î/ìîÑ®/–¸^O_>õëùæeõþ¼Òr¦Ó­í÷/»×+ ¼~Qºz<„ëp÷,|¼¹²“Ü«íöû«ƒý£Ç[{|Úí—ß>.‡xûCÁz½bûû|º}ôó[>ýù¼òèORr>›<ýRÿb&o""",'L1')
assert hashlib.md5(b).hexdigest()=='c0c42cbe7318e7e7d9c58ca4800e9681','corrupted, you may have broke it during re-saving'
exec(zlib.decompress(b))
