<template>
  <div id="app">
    <div style="width: 55%; float: left;">
      <table border="1" width="800" height="510" style="border-radius: 10px;">
        <tbody style="border: 2px;"><tr>
          <td colspan="2" align="center" style="border: hidden;">
          <br> Followers : 0명 
          </td>
          <td style="border: hidden;">
            <br>
            <span class="user_title" style="font-weight: bold; margin-left: 10px;">김00 님의 영화</span>
          </td>
        </tr>
        <tr>
          <td width="10" style="border: hidden;"></td>
          <td width="178" height="450" style="border-width: 1px; border-style: solid; border-color: gray white gray gray; border-image: initial; border-radius: 10px; vertical-align: top;">
            <table width="130">
              <div style="border-right: hidden;">
                <br>
                <tr align="center">
                  <select name="feeling" style="width: 120px; text-align: center;">
                    <option value="happy"><img src="#">행복</option>
                    <option value="sad">슬픔</option>
                    <option value="anger">분노</option>
                    <option value=""></option>
                    <option value=""></option>
                  </select>
                </tr>
                <br>
                <tr>
                  <td>
                    <table width="160" cellpadding="1" cellspacing="1">
                      <img src="/img/profile.png" width="170" height="150" border="0">
                    </table>
                  </td>
                </tr>
                <br>
                <div style="height: 120px;">
                  <tr align="center"> 여기는 그냥 글인데 뭘 적어야 할지 모르겠음 </tr>
                </div>
                <hr>
                <div style="font-size: 12px;"> 김00 (genre) 0 Followers </div>
              </div>
            </table>
          </td>
          <td width="480" height="450" style="overflow-y: scroll; border-width: 1px; border-style: solid; border-color: gray gray gray white; border-image: initial; border-radius: 10px;">
            <div class="container">
              <div class="row row-cols-2 row-cols-md-4 g-4">
                <!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }--><!--function (a, b, c, d) { return createElement(vm, a, b, c, d, true); }-->
                <router-view/>
              </div>
            </div> 영화추천 
          </td>
          <div>
            <td style="vertical-align: top; padding-top: 30px; border: hidden;">
              <div>
                <router-link to='/' style="font-size: 10px; text-decoration-line: none;"><div class="menu">홈</div></router-link>
                <router-link to="/random" style="font-size: 10px; text-decoration-line: none;"><div  class="menu">추천 영화</div></router-link>
                <router-link to="/my-movie-list"  style="font-size: 10px; text-decoration-line: none;"><div class="menu">플레이 리스트</div></router-link>
                <router-link to="/community"  style="font-size: 10px; text-decoration-line: none;"><div class="menu">게시판</div></router-link>
                <router-link to="/search"  style="font-size: 10px; text-decoration-line: none;"><div  class="menu">검색</div></router-link>
              </div>
            </td>
          </div>
        </tr>
      </tbody>
    </table>
  </div>
  
  <div style="float: left; border: 2px groove; width: 150px; height: 200px; border-radius: 10px;">
    <div></div>
  </div>
</div>
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 60px;
}

div > td > div div {
    width: 90px;
    height: 35px;
    border: 1px solid black;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #20B2AA;
    border-radius: 0px 7px 7px 0px;
    margin-bottom: 5px;
    border-left-color: white;
}
</style>
