<h1 align="center">StableHorde-text-template-py</h1>
<h3 align="center">Bulky template for generating text with StableHorde. <code>text_generation.py</code></h3>

<p align="center">Sample file is <code>main.py</code>. <code>text_generation.py</code> is the main generation file. <code>main.py</code> tells you how to use it, <code>text_generation.py</code> is it.</p>

<p align="center"><strong>Parameters you HAVE TO use:</strong></p>
<ul align="center">
  <li>chat - True or False. if True, only use Pygmalion models. If False, never use Pygmalion models.</li>
  <li>prompt - The prompt. A string.</li>
  <li>printing - True or False. Debugging purposes. If True, prints everything, if False, prints nothing.</li>
  <li>timeout - How long until it timeouts. A number. Sometimes requests get stuck, so this is important.</li>
</ul>

<p align="center">Profanity filters are on by default for <code>text_generation.py</code>, but can be disabled by simply replacing <code>return "The AI's response contained inappropriate content. Please rephrase your input.", True</code> with <code>return text, False</code>.</p>

<p align="center">Have fun!</p>
