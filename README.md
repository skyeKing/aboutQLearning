# aboutQLearning<br>
开始学习Qlearning<br>
<h3>Qlearning 转移方程</h3><br>
<h4>Q(s,a) = R(s,a) + gamma*max{Q(s~,a~)}</h4><br>
<ul>
  <li>s为state的简写，意为状态。在这个公式中为当前所处的状态状态</li>
  <li>a为action的简写，意为行为、行动。在这个公式中为当初在状态s，所采取的行动</li>
  <li>Q为Q表(Q tabel)，是由状态和其对应的行动所组成的表格，一般Q表在程序执行开始前会进行初始化，初始化为0。<b>--</b> 行数为状态数目，<b>|</b>列数 (注意区分：tabel 表 table 桌子)</li>
  <li>R为R表(reward,奖励)，跟Q表结构一致。不过其中的值为规定好的值（暂时未常数）</li>
  <li>s~为当状态为s，并采取了行为a之后所处的状态</li>
  <li>a~为当状态为s~，采取了行为</li>
  <li>max{}表示 找到尖括号中的最大值，max{}的值为最大值的值</li>
  <li>max{Q(s~,a~)} 当处于s~状态时，找到其允许的a~，从而求出Q(s~,a~)的一系列的值，然后只留最大的值，参与运算</li>
  <li>gamma(discount factor)为贪婪因子、折扣因子。数学表示为<b>γ</b>。使用γ与预期最大的Q(s~,a~)相乘来控制以往的经验对当前行为产生的影响，当γ越大，表示Q(s,a)的值受以前经验影响越大(长远利益)；反之越小，越注重眼前利益</li>
</ul>
Qlearning 算法<br>
<ol>
  <li></li>
