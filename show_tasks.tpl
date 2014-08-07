<html>
    <head>
        <title>Sean's To Do List</title>
        <style>
            html, body, div, span, applet, object, iframe,
            h1, h2, h3, h4, h5, h6, p, blockquote, pre,
            a, abbr, acronym, address, big, cite, code,
            del, dfn, em, img, ins, kbd, q, s, samp,
            small, strike, strong, sub, sup, tt, var,
            b, u, i, center,
            dl, dt, dd, ol, ul, li,
            fieldset, form, label, legend,
            table, caption, tbody, tfoot, thead, tr, th, td,
            article, aside, canvas, details, embed, 
            figure, figcaption, footer, header, hgroup, 
            menu, nav, output, ruby, section, summary,
            time, mark, audio, video {
                margin: 0;
                padding: 0;
                border: 0;
                font-size: 100%;
                font: inherit;
            }
            article, aside, details, figcaption, figure, 
            footer, header, hgroup, menu, nav, section {
                display: block;
            }
            body {
                line-height: 1;
            }
            ol, ul {
                list-style: none;
            }
            blockquote, q {
                quotes: none;
            }
            blockquote:before, blockquote:after,
            q:before, q:after {
                content: '';
                content: none;
            }
            table {
                border-collapse: collapse;
                border-spacing: 0;
            }
        </style>
    </head/>
    <center>
    <body style="background-color:FCF0AD;">
        <p style="padding-top: 20px; padding-bottom:10px; font-size:80px;">Sean's To Do List</p>
        <table border="2">
        %for row in rows:
          <tr>
            <td style="font-size:40px;">{{row[1]}} Due {{row[2]}}</td>
                <td style="padding-left:15px;">
                    <form action="http://127.0.0.1:8080/todo/edit/{{row[0]}}">
                        <input type="submit" value="Edit" style="font-size:20px; width:60px; height:32px;">
                    </form>
                </td> 
          </tr>
        %end
        </table>
        <form action="http://127.0.0.1:8080/todo/new", style="padding-top:10px;">
            <input type="submit" value="Add" style="font-size:20px; width:80px; height:40px;">
        </form>
    </body>
    </center>
</html>
