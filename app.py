import streamlit as st
st.sidebar.title("Players")
section=st.sidebar.radio("Category:",["The Goats","Legends","Icons","Modern Era"])
st.title("Welcome to Football Fever") 

if(section=="The Goats"):
  st.title("The Goats")
  col1,col2=st.columns(2)
  with col1:
    st.image("https://imgs.search.brave.com/2HT4xzoSCYvnuBxEGPCERt5clNBnnIPoc0JsiBhoLUg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjE2/ODI2NzA2NC9waG90/by90b3BzaG90LXBv/cnR1Z2Fscy1uYXRp/b25hbC10ZWFtLXBs/YXllci1hbmQtc2F1/ZGktYWwtbmFzc3Jz/LWZvcndhcmQtY3Jp/c3RpYW5vLXJvbmFs/ZG8taG9sZHMuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPVZE/UE4tTHI0Z3ZiMW44/M3A3Tmt1OTlTN2p2/SjJWa0lRRldaSGRv/eVhIc2c9",width=300)
    st.text("Name: Cristiano Ronaldo")
    button=st.button("GOAT")
    if(button):
      st.success("He is the GOAT")
    st.text("Career stats : ")
    st.text("1000 goals")
    st.text("5 Ballondors")
    st.text("5 UCL")
    st.text("Trophies:34")
  with col2:
    st.image("https://imgs.search.brave.com/1qe721d9LJe6fnXG53WtRN-kaB58ZcWofQM6sz3ZStI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/c2kuY29tLy5pbWFn/ZS90X3NoYXJlL01U/WTRNVEF5TlRjME56/ZzNOREExTURjei9t/ZXNzaS1qZXJzZXkt/cmVhbC1tYWRyaWRq/cGcuanBn",width=300)
    st.text("Name: Lionel Messi")
    if(st.button("Goat")):
      st.success("He is the GOAT")
    st.text("Career stats : ")
    st.text("900 goals")
    st.text("8 Ballondors")
    st.text("4 UCL")
    st.text("Trophies:48")

elif(section=="Legends"):
  st.title("Legends")
  col1,col2=st.columns(2)
  with col1:
    st.image("https://imgs.search.brave.com/E-cN7OPFPqONjBcGvFeV7V6pUIz_mB9gJdkBdEwOkZ0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9wZW9w/bGUuY29tL3RobWIv/OFA4Ml85VmFNR1ha/RHcwMEpSeTFfSE93/a1hJPS80MDAweDAv/ZmlsdGVyczpub191/cHNjYWxlKCk6bWF4/X2J5dGVzKDE1MDAw/MCk6c3RyaXBfaWNj/KCk6Zm9jYWwoODM5/eDM1OTo4NDF4MzYx/KS8xLXBlbGUteW91/bmctMTk2MS02Y2Fj/Mjk0MGUzYmY0YTQ5/YWZlMzMyMzlhNjY3/ZmMxNS5qcGc",width=300)
    st.text("Name: Pele The god")
    st.text("Career stats:")
    st.text("757 goals")
    st.text("3 World Cups")
    st.text("2 times Copa roca Winner")
    st.text("6 titles with santos")

    st.image("https://imgs.search.brave.com/22eC4SZybMHpYa2trNlZ_B7MPpMThKC1beSMIGW4evY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTA4/MDc1MTAwMC9waG90/by9sZS1taWxpZXUt/ZGUtdGVycmFpbi1m/cmFuJUMzJUE3YWlz/LXppbmVkaW5lLXpp/ZGFuZS1wciVDMyVB/OXNlbnRlLWF1LXB1/YmxpYy1zb24tYmFs/bG9uLWRvci0xOTk4/LWxlLTIwLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1KRk5p/ZVBEX05ZVWZ6b21m/dGZUS3p1VldQbXRJ/OTA4ZVNfSHNfMTVt/ekZFPQ",width=300)
    st.text("Name: Zinedine Zidane")
    st.text("Career stats:")
    st.text("156 goals & 169 assists")
    st.text("1 World Cup")
    st.text("1 Ballondor")
    st.text("1 UCL")

    st.image("https://imgs.search.brave.com/s_N-MJcw1LS2WxiVm0yi6JlvOBXrn_wIFY58wn_kxTg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy83/LzdjL0pvaGFuX0Ny/dXlmZl9pbl90cmFp/bmluZ3NwYWtfTmVk/ZXJsYW5kc19FbGZ0/YWxfLF9rb3AuanBn",width=300)
    st.text("Name: Johan Cruyff")
    st.text("Career stats:")
    st.text("340 goals")
    st.text("4 times dutch footballer of the year")
    st.text("3Ballondor's")
    st.text("4 times La Liga Winner as a Manager")

    st.image("https://imgs.search.brave.com/Aba25GNYpbz1BCzFUcyq0LDkJYW_Jdl-E0ZYj1vjTX8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9saWJy/YXJ5LnNwb3J0aW5n/bmV3cy5jb20vc3R5/bGVzL2Nyb3Bfc3R5/bGVfMTZfOV9kZXNr/dG9wX3dlYnAvczMv/MjAyNC0wMS9uYmEt/cGxhaW4tLWZlMTMz/MDE0LTVjNzYtNDZl/Yy04ODkwLTY2NjZi/YmNkZDFkZi5qcGVn/LndlYnA",width=300)
    st.text("Name:Franz beckenbauer")
    st.text("Career stats: ")
    st.text("75 goals")
    st.text("World cup Winner")
    st.text("Europena championship winner")
    
  with col2:
      st.text("Name:Diego Maradona")
      st.image("https://imgs.search.brave.com/YcOeOTdd4D4oA0lWXfNb7KCBz8hzOx-2LgfoX4Z2zeI/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuZ29hbC5jb20v/aW1hZ2VzL3YzL2dl/dHR5LTk4NDk0OTk3/OC9jcm9wL01NNURF/TkpRR0U1RENOQlFH/NDVHNDMzWE1VNURB/T1JSR00zUT09PT0v/R2V0dHlJbWFnZXMt/OTg0OTQ5OTc4Lmpw/Zz9hdXRvPXdlYnAm/Zm9ybWF0PXBqcGcm/d2lkdGg9Mzg0MCZx/dWFsaXR5PTYw",width=300)
      st.text("Career stats: ")
      st.text("348 goals")
      st.text("World cup Winner")
      st.text("Serie a Winner")
      
      st.text("Name:Ronaldo Nazario")
      st.image("https://imgs.search.brave.com/ogPxgfm5JTIwpW4yO-HPGQfWOjo4HNq4ZjMUm17sUik/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuc3F1YXJlc3Bh/Y2UtY2RuLmNvbS9j/b250ZW50L3YxLzY0/MTVjMjUxYjE1MWM0/MDQ5NWI2MGNlMC9m/NDQ2YWU2NC1iMGNh/LTRlNmUtOTdmMi01/NTRjMDc3N2E1ZDQv/Um9uYWxkbytTY3Jl/ZW5zaG90KzIwMjMt/MDMtMjQrLnBuZw",width=300)
      st.text("Career stats: ")
      st.text("414 goals")
      st.text("World cup Winner")
      st.text("2 times Ballondor winner")
      st.text("La Liga Winner")

      st.text("Name:Ricardo Kaka")
      st.image("https://imgs.search.brave.com/Pr_mFRh_7AbftQrKlXqMa1tlC3DOiJya4hEAB0_pzH4/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNDgx/MzMzNzIxL3Bob3Rv/L21pbGFuLWl0YWx5/LWtha2Etb2YtYWMt/bWlsYW4tY2VsZWJy/YXRlcy1zY29yaW5n/LXRoZS10aGlyZC1n/b2FsLWR1cmluZy10/aGUtc2VyaWUtYS1t/YXRjaC5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9SkRsdEN2/bUpoaUFEYXRnc1NJ/c2lKMDlWR2Nkd0U4/LTZfbDl1Vzdfdjh4/cz0",width=300)
      st.text("Career stats: ")
      st.text("240 goals")
      st.text("World cup Winner")
      st.text("Ballondor winner")
      st.text("UCL Winner")

      st.text("Name:Marco Van Basten")
      st.image("https://imgs.search.brave.com/urACdgK2gHI91SYarakfkqdHfBu3eQlPO-EMFU2b_M0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJzLmNvbS9p/bWFnZXMvaGQvbWFy/Y28tdmFuLWJhc3Rl/bi1zbWlsaW5nLWxp/ZnRpbmctdHJvcGh5/LTR2ZWVud3Flbnhw/dWthM2guanBn",width=300)
      st.text("Career stats: ")
      st.text("277 goals")
      st.text("Euro Winner")
      st.text("3 times Ballondor winner")
      st.text("UCL Winner")

elif(section=="Icons"):
  st.title("Icons")
  col1,col2=st.columns(2)
  with col1:
    
    st.text("Name: Toni Kroos")
    st.image("https://imgs.search.brave.com/gItSXvtIOprv5BTkuNfi5h6GIK78wjix1sA_un3G5w8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjE2/MDc4MTgzNi9waG90/by9zdHV0dGdhcnQt/Z2VybWFueS10b25p/LWtyb29zLW9mLWdl/cm1hbnktYXBwbGF1/ZHMtdGhlLWZhbnMt/YWZ0ZXItdGhlLXVl/ZmEtZXVyby0yMDI0/LXF1YXJ0ZXIuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPWtG/ZmRjWGdOUENSTE1k/YzdJRHI1cDhzQkd4/Mk9oX21fczVzdTVj/dlVHd0k9",width=300)
    st.text("Career stats:")
    st.text("140 goals & 190 assists")
    st.text("World Cup Winner")
    st.text("4 La Liga Titles")
    st.text("6 UCL")

    
    st.text("Name:Marcelo")
    st.image("https://imgs.search.brave.com/tRbAE13qeURydxwblZrJYjPytRSP1gmCb2mb_7UvtoM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTI0/MDk2NTAyMS9pdC9m/b3RvL3RvcHNob3Qt/cmVhbC1tYWRyaWRz/LWJyYXppbGlhbi1k/ZWZlbmRlci1tYXJj/ZWxvLWNlbGVicmF0/ZXMtd2l0aC10aGUt/Y2hhbXBpb25zLWxl/YWd1ZS10cm9waHku/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PTEtQVhSUWx5TUdJ/RlNBVzNlMEJzdTY5/ZE9saW80TkxBalJD/SVYzc3F1MEE9",width=300)
    st.text("Career stats:")
    st.text("38 goals & 120 assists")
    st.text("4 La Liga Titles")
    st.text("5 UCL")
    st.text("Club World Winner")

  
    st.text("Name:Sergio Ramos")
    st.image("https://imgs.search.brave.com/mIHuSXZT98eV0zYMIwZiUGPa3nIhUHpucqiK_e6wSsw/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTI1/MzkzNjM1OC9waG90/by9tYWRyaWQtc3Bh/aW4tc2VyZ2lvLXJh/bW9zLW9mLXJlYWwt/bWFkcmlkLWNlbGVi/cmF0ZXMtaGlzLXRl/YW1zLWZpcnN0LWdv/YWwtZHVyaW5nLXRo/ZS1saWdhLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1lM1p6/enRsMmJSaGJMZl9p/Y0c0LURNUmg4dmo2/SEZzYzdRRWVkSm1l/eFNvPQ",width=300)
    st.text("Career stats:")
    st.text("140 goals")
    st.text("5 La Liga titles")
    st.text("4 UCL")
    

   
    st.text("Name:Xavi Hernandez")
    st.image("https://imgs.search.brave.com/iD32LKk8ivAw7bYTyuWrIvKMA-N7fBqlgD8Fdk7XgSQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi94YXZp/LWhlcm5hbmRlei1i/YXJjZWxvbmEtMTk1/NzczOTkuanBn",width=300)
    st.text("Career stats: ")
    st.text("120 goals & 230 assists")
    st.text("World cup Winner")
    st.text("8 La Liga Titles")
    st.text("4 UCL")
    
  with col2:
      st.text("Name:Iniesta")
      st.image("https://imgs.search.brave.com/gkwb2AgOeEpcL3ByoSCBiGMlc1T2J31DdVB-2M99TMA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9hbmRy/JUMzJUE5cy1pbmll/c3RhLWZjLWJhcmNl/bG9uYS1mcmllbmRs/eS1mb290YmFsbC1t/YXRjaC1mYy1kaW5h/bW8tYnVjaGFyZXN0/LWZjLWJhcmNlbG9u/YS10aC1hdWd1c3Qt/MzIyNjE5ODEuanBn",width=300)
      st.text("Career stats: ")
      st.text("100 goals & 190 assists")
      st.text("World cup Winner")
      st.text("9 La Liga Titles")
      st.text("4 UCL")
      
      st.text("Name:David Beckham")
      st.image("https://imgs.search.brave.com/MpQHy8GqrZGWeAHPhKxDl8wMfrH8IwlPR27XFj1Jj3g/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjUz/MDUxNi9waG90by9t/YWRyaWQtZGF2aWQt/YmVja2hhbS1vZi1y/ZWFsLW1hZHJpZC1j/ZWxlYnJhdGVzLXJl/YWwtbWFkcmlkcy1v/cGVuaW5nLWdvYWwt/ZHVyaW5nLXRoZS11/ZWZhLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1xRDE2Y0do/MnB2THM1MXk0ZmdY/YXpXcTdFckNqWl9j/cHB4V3ZBWWpoT3hN/PQ",width=300)
      st.text("Career stats: ")
      st.text("127 goals")
      st.text("6 Premiere titles")
      st.text("UCL Winner")
      st.text("La Liga Winner")
    

      st.text("Name:Thiery Henry")
      st.image("https://imgs.search.brave.com/y-3JFczbHgOUKnzKIwFUNIuNMddRdt2nKgUpNWuM9eI/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMuaW5kZXBlbmRl/bnQuY28udWsvMjAy/NS8wNC8wOS8xMi8x/MzNjOGIxMmYyMTBh/OWZlMjQ0ZDIwMDY3/NDc2Yzg1ZlkyOXVk/R1Z1ZEhObFlYSmph/R0Z3YVN3eE56UTBN/amd5T0RrMS0yLjI5/Mzc2MTQuanBnP3F1/YWxpdHk9NzUmd2lk/dGg9NjQwJmF1dG89/d2VicA",width=300)
      st.text("Career stats: ")
      st.text("380 goals")
      st.text("World cup Winner")
      st.text("2 Premier League titles")
      st.text("La Liga Winner")

      st.text("Name:Zlantan")
      st.image("https://imgs.search.brave.com/VvbVscfBGWCQdKG_MU0-sMNzj35KgABc57y2lwUsMS8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzYzL2Ey/LzU5LzYzYTI1OTgw/ZTI4OTVjNTVjYjY0/ZjhjZmU2NTJmNDRk/LmpwZw",width=300)
      st.text("Career stats: ")
      st.text("570 goals")
      st.text("4 Seria A titles")
      st.text("4 League 1 titles")
      st.text("Club World Cup Winner")

elif(section=="Modern Era"):
  st.title("Modern Era")
  col1,col2=st.columns(2)
  with col1:
    
    st.text("Name:Kylian Mbappe")
    st.image("https://imgs.search.brave.com/q6k80e80i4-72IaQBANPIbg50PgCTk-ilV6kq7SysM0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjE2/MjM3Njc1MC9waG90/by9tYWRyaWQtc3Bh/aW4tcmVhbC1tYWRy/aWQtbmV3LXNpZ25p/bmcta3lsaWFuLW1i/YXBwZS1pcy11bnZl/aWxlZC1hdC1lc3Rh/ZGlvLXNhbnRpYWdv/LWJlcm5hYmV1Lmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz03/VFN6VV9IMmx2YzRn/SkdfYmdlclVPY19U/am9hU09tQXFyNTVW/T21Bb2RBPQ",width=300)
    st.text("Career stats:")
    st.text("418 goals & 170 assists")
    st.text("World Cup Winner")
    st.text("3 League 1 titles")
    st.text("UCL Winner")

    
    st.text("Name:Erling Haaland")
    st.image("https://imgs.search.brave.com/4B2FWwMOknixIgyVQxyR4FNozrzqdM9PJg99t7MeWlo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ5/NDA1Nzk3NS9waG90/by9icmVudGZvcmQt/ZW5nbGFuZC1lcmxp/bmctaGFhbGFuZC1v/Zi1tYW5jaGVzdGVy/LWNpdHktcG9zZXMt/Zm9yLWEtcGhvdG8t/YWZ0ZXItYmVpbmct/YXdhcmRlZC10aGUu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PXlCVlF2ekc2bkJ6/MjFpUHVqV2FoVjY2/ckFZZGVrWFFodmZC/WkV3TUJ5WEE9",width=300)
    st.text("Career stats:")
    st.text("210 goals& 50 assists")
    st.text("Premiere League Winner")
    st.text("UCL Winner")
    st.text("FA Cup Winner")

  
    st.text("Name:Lamine Yamal")
    st.image("https://imgs.search.brave.com/8IpGe-ZY3KZL1M81NoQJ3jBUDc2pP-XXQf46zl1IHbw/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjIx/MjE0OTk1My9waG90/by9zZXZpbGxlLXNw/YWluLWxhbWluZS15/YW1hbC1vZi1mYy1i/YXJjZWxvbmEtY2Vs/ZWJyYXRlcy1hZnRl/ci10aGUtdGVhbXMt/dmljdG9yeS1pbi10/aGUtY29wYS1kZWwu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PUc2TTRkNGxlaFpT/bmtEZ2x5dnZKekZQ/dGNnNzNWajBzWGhH/RDY4Qi00Y289",width=300)
    st.text("Career stats:")
    st.text("25 goals & 30 assists")
    st.text("Euro Winner")
    st.text("La Liga Winner")
    

   
    st.text("Name:JudeBellingham")
    st.image("https://imgs.search.brave.com/C8A4x472chu_kpTIUb7w9KH_VRlDbde5xVsXqk5IDFY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgy/MDkzMDAxMy9waG90/by9tYWRyaWQtc3Bh/aW4tanVkZS1iZWxs/aW5naGFtLW9mLXJl/YWwtbWFkcmlkLWNl/bGVicmF0ZXMtYWZ0/ZXItc2NvcmluZy10/aGUtdGVhbXMtc2Vj/b25kLWdvYWwuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPXBX/Nk93Q045TFZraGxy/S0xQZVVMN0JZcnN6/R180TjJYQVJWN0FV/SGRWblk9",width=300)
    st.text("75 goals 62 assists")
    st.text("La Liga Winner")
    st.text("SuperCup Winner")
    st.text("UCL Winner")
    
  with col2:
      st.text("Name:Michael Olise")
      st.image("https://imgs.search.brave.com/gg4sj_QRjp-9SWuNi6Q2M3OgkqJI9n2een5knSR1izw/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjIx/MzIwMTg2Ny9waG90/by9sZWlwemlnLWdl/cm1hbnktbWljaGFl/bC1vbGlzZS1vZi1i/YXllcm4tbXVuaWNo/LWNlbGVicmF0ZXMt/c2NvcmluZy1oaXMt/dGVhbXMtc2Vjb25k/LWdvYWwuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPUFmS3ZL/eXVvRG5aNHJIV3o4/LXN3T3ZoaXFJT0xZ/UmlpSUJDTHg5SWQw/MG89",width=300)
      st.text("Career stats: ")
      st.text("100 goals & 190 assists")
      st.text("Bundesliga Winner")
      st.text("50 goals")
      st.text("DFL SuperCup")
      
      st.text("Name:Vini.Junior")
      st.image("https://imgs.search.brave.com/5FpYM5kcSSD2ecL3R1BydRGMUQ5iDi6glMfxoz6silQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTkz/Mjk0ODM2OS9waG90/by9yaXlhZGgtc2F1/ZGktYXJhYmlhLXZp/bmljaXVzLWp1bmlv/ci1vZi1yZWFsLW1h/ZHJpZC1jZWxlYnJh/dGVzLWFmdGVyLXNj/b3JpbmctdGhlaXIt/dGVhbXMtZmlyc3Qu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PUZMbkhUcTYydlUt/WkQ4Nmh6QVFuOUo4/dzRxemc2b09uZ2FK/d0JSTHR4U0k9",width=300)
      st.text("115 goals & 90 assists")
      st.text("La Liga Winner")
      st.text("2 UCL titles")
      st.text("SuperCup Winner")
    

      st.text("Name:Dembele")
      st.image("https://imgs.search.brave.com/2J_yt_6JzFWCGWGCm4H-gFve3PTydOWVzeCkcuHEx7k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/YWxqYXplZXJhLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/NS8wOS8yMDI1LTA5/LTIyVDIxMDUxOFpf/MTY2NjkxNTkxOF9V/UDFFTDlNMU1LVDkx/X1JUUk1BRFBfM19T/T0NDRVItQkFMTE9O/LTE3NTg1ODE4MzIu/anBnP3c9NzcwJnJl/c2l6ZT03NzAsNDk2/JnF1YWxpdHk9ODA",width=300)
      st.text("Career stats: ")
      st.text("150 goals")
      st.text("UCL Winner")
      st.text("League 1 Winner")
      st.text("Super Cup Winner")
      st.text("Copa De France Winner")

      st.text("Name:Nuno Mendes")
      st.image("https://imgs.search.brave.com/ZX8shAwoVSEtxpZUuWWLx5MgMZWPA6iNlmatYCMDIVM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9ha2Nk/bi5kZXRpay5uZXQu/aWQvY29tbXVuaXR5/L21lZGlhL3Zpc3Vh/bC8yMDI1LzA2LzA5/L251bm8tbWVuZGVz/LTE3NDk0MjY1MTM5/NzAuanBlZz93PTcw/MCZxPTkw",width=300)
      st.text("Career stats: ")
      st.text("20 goals and 30 assists")
      st.text("UCL Winner")
      st.text("League 1 Winner")
      st.text("Super Cup Winner")
      st.text("Copa de France Winner")
  


   
 




   
