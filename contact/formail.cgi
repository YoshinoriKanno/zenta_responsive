#! /usr/bin/perl

;# ↑ Perl処理系のパスを指定。不明な場合はプロバイダかサーバー管理者に確認。

;#   <iMODE/J-SKY対応> フォームメール [フォーメール SE] 
;#    - Version 3.03 / Jul 27, 2004
;#    - Copyright(C)2004 WEB POWER. All Rights Reserved.
;#    - 最新版・最新情報は <http://www-power.net/>

Show_File_by_CGI($1) if ($ENV{'QUERY_STRING'} =~ /^\[(\w+)\]$/);
#BEGIN_INIT
#-----------------------------------------------------------------------------#
# ここから初期設定です（サーバーへの設置方法は同梱のマニュアルをご覧下さい）  #
#-----------------------------------------------------------------------------#
#
# <<注意事項>>
#  * 数字以外は''内に記述します。'を入れたい場合は 中の'は \'にしてください。
#      ex) × $var = value;  →  ○ $var = 'value';
#      ex) × $var = 'I can't';  →  ○ $var = 'I can\'t';
#  * $ # ; ' 等の記号は間違って消さないように注意してください。
#  * 1文字のミスでもプログラムは動きません。設定・編集は慎重にしましょう。
#  * 行の頭に"#"を付けると、その行は無効になります。(コメントアウト)
#  * 値を設定しない場合は、''かコメントアウトしてください。
#      ex) × $var = ;  →  ○ $var = '';
#  * 初期設定以外の部分を1バイトでも変更した場合の動作保証は一切しません。
#  * 詳しくは本サイトの解説/FAQ等を参照してください。
#  * 漢字コードは自動認識ですが、携帯電話で使う場合は"SHIFT_JIS"専用です。


#=> メールの送信先を固定する場合はそのアドレスを指定してください。
#  * ここで指定すると、送信者に送信される控えメールを除いて、このアドレス以外
#    には送信しません。フォームからの"_mailto"は無視されます。
#  * (重要)テスト送信する場合でも必ず存在する有効なアドレス(自分宛)にしてくだ
#    さい。適当なアドレスに送信すると、関係のない所にメールが届いたり、エラー
#    メールの発生により第三者に迷惑がかかります。
$INI{'mailto'} = 'shiina@zenta1.com';

#=> ファイルアップロードを許可 (1:する／0:しない)
#  * 許可しない場合、マルチパートフォームデータが送信されてもエラーを返します。
#  * リクエストメソッドが'GET'の場合は使えません。
$SYS{'UseMultipart'} = 0;

#=> POSTメソッドで受け取る最大容量[キロバイト]
#  * サーバー、クライアントが対応していればプログラム的には上限はありません。
#  * サーバー等への負荷を考慮して、あまり大きくしないようにしてください。
$SYS{'maxsize'} = 1024;#キロバイト


#=> タイムゾーン
#  * GMT(グリニッジ標準時=英国ロンドン)との時差 (日本は9時間)
$INI{'TimeZone'} = 9;


#---<パス/URLの設定>-----------------------------------------------------------
#
#   * パス、URLはすべて半角で指定してください。(全角は一切使えません)
#   * [パス]とはサーバー内での場所です。http://で始まるURLとは違うものです。
#   * 相対パスとはスクリプトの場所を基準としたパスの指定です。
#      ../ => 1つ上のディレクトリ  ./ => 同じディレクトリ
#   * 絶対パスとはサーバー内の一番上のディレクトリを基準としたパスの指定です。
#       /usr/lib/sendmail  /home/foo/public_html/cgi-bin/script.cgi
#   * 仮想アドレスとはURLの一部分(ドメイン名以降)を指します。
#       http://www.domain.com/~foo/cgi-bin/script.cgi
#                            ^ ドメイン名の後のスラッシュ"/"以降の部分
#                              (/~foo/cgi-bin/script.cgi のこと)


#=> ライブラリ(stdio.pl)の[パス]
$SYS{'stdiopl'}  = 'stdio.pl';

#=> ライブラリ(jcode.pl)の[パス]
$SYS{'jcodepl'}  = 'jcode.pl';

#=> メール送信コマンド(sendmail)の[パス]
$SYS{'sendmail'} = '/usr/sbin/sendmail';

#=> テンポラリファイル用ディレクトリの[パス]
#  * このディレクトリのパーミッションは[777]にする。
$SYS{'TempDir'} = 'tmp/';

#=> 送信者向け添付ファイル格納ディレクトリの[パス]
#  * 送信者宛にファイルを添付したメールを送信する場合、その添付ファイルがあるデ
#    ィレクトリのパスを指定します。
#  * 送信者からファイルをアップロードしてもらうだけの場合は設定不要です。
$SYS{'FileDir'} = 'file/';

#=> データディレクトリのパス
#  * このディレクトリのパーミッションは[777]にする。
$SYS{'DataDir'} = 'data/';

#=> データファイルのURL(↑のパスをhttp://で指定)
$SYS{'DataDirURI'} = 'http://サーバー/パス/data/';

#=> 添付ファイルはメールに添付せずにサーバー上に保存 (1:する／0:しない)
#  * メールには保存先のURIが挿入されます。1Mを超えるようなファイルを受け取る場合は、
#    メール添付は避け、サーバー上に保存するようにしましょう。
$INI{'NoAttach'} = 0;

#=> タイトル (TITLE要素等で表示)
$INI{'Title'} = 'フォーメール';

# ○ フォームページのURL (このURL以外からは送信できない。%7Eは~と書く)
#$INI{'SetUrl'} = 'webpower.jp/';


#---<デザイン設定>-------------------------------------------------------------


#=> BODY要素の属性 (<BODY ****>の****の部分)
$INI{'body'} = 'text="#000000" bgcolor="#FFEEDD"';

# ○ 外部CSSファイルの[アドレス]
$INI{'css'} = '';

# ○ 確認ページのテーブルの項目名の背景色
$INI{'BG-COLOR1'} = '#99CCFF';

# ○ 確認ページのテーブルの項目の背景色
$INI{'BG-COLOR2'} = '#FFFFCC';

#=> 確認ページ上部に表示するHTML (_EOF_行は削除しない)
$INI{'header'} = <<'_EOF_';

<h1>送信内容確認</h1>

_EOF_

# ○ CSS定義 (STYLE要素の内容/_EOF_行は削除しない)


#---<特殊な設定>---------------------------------------------------------------
#
#   一般的なサーバーでは初期状態のままで問題ありません。
#   必要に応じて設定してください。


#=> リクエストメソッド (POST／GET)
#  * 送信後 'Method not implemented'等のエラーが出る場合は'GET'にしてください。
#  * 'GET'の場合は文字制限があるため、長い文章等は途中で切れる場合があります。
#  * J-SKYからアクセスの場合は、ここでの設定に関係なく自動的に'GET'になります。
$SYS{'rmethod'} = 'POST';

#=> このスクリプトの設置URL (http://で指定)
#  * CGI-WRAP等を採用しているサーバー(interQ等)は設定してください。
#$SENV{'SERVER_URI'} = 'http://www.domain.ne.jp/~foo/cgi-bin/formail.cgi';


#END_OF_INIT
#==============================================================================
# ● メインルーチン (初期設定ここまで。以下修正不要。修正した場合は動作非保証)
#==============================================================================


# <各種設定・初期化>
#sub init
{

    binmode STDOUT;              #  Windows系OSの場合は下の行のコメントを解除
    $VERSION = q$FORMAIL/3.03$;  #  ヴァージョン情報(編集禁止)

    #  ライブラリロード
    if (!-f $SYS{'jcodepl'}) {
        Show_ErrorPage('[001]ライブラリ未検出',
                       'ライブラリが見つかりません',
                       '<p>　このシステムを動作させるのに必要なライブラリ[jcode.pl]が見つかりません。所定の場所に存在しているか、場所の指定は正しいかを確認してください。</p>');
    }
    if (!-f $SYS{'stdiopl'}) {
        Show_ErrorPage('[002]ライブラリ未検出',
                       'ライブラリが見つかりません',
                       '<p>　このシステムを動作させるのに必要なライブラリ[stdio.pl]が見つかりません。所定の場所に存在しているか、場所の指定は正しいかを確認してください。</p>');
    }
    require $SYS{'stdiopl'};
    require $SYS{'jcodepl'};

    if ((split(/\//, $stdio::version))[1] < 9.04) {
        Show_ErrorPage('[002]ライブラリバージョンエラー',
                       'ライブラリのバージョンが違います',
                       '<p>　このシステムを動作させるのに必要なライブラリ[stdio.pl]は、v9.04以降を使用してください。</p>');
    }


    #  stdio.pl初期設定
    $stdio::max_byte = $SYS{'maxsize'} * 1024;  # 受信可能最大容量 (キロバイト)
    $stdio::sendmail = $SYS{'sendmail'};        # sendmailのパス


    #  ソースコードの漢字コード認識
    if (ord "漢" == 0xb4 || ord "漢"  == -76) {
        $JCODE = "euc";
        $CHARSET = '; charset=EUC-JP';
    } elsif (ord "漢" == 0x8a || ord "漢" == -118) {
        $JCODE = "sjis";
        $CHARSET = '; charset=Shift_JIS';
    } elsif (ord "漢"  == 0x1b) {
        $JCODE = "jis";
        $CHARSET = '; charset=ISO-2022-JP';
    }

    #  環境変数 / 標準入力データ設定
    %SENV = %STDIO = ();
    @FORM_DATA = &stdio::getFormData(\%STDIO, 2, $JCODE, "\t", $SYS{'TempDir'});
    $SENV{'HTTP_REFERER'} = substr($ENV{'HTTP_REFERER'}, 0, 200);
    $SENV{'HTTP_REFERER'} =~ s/%7E/~/gi;
    $SENV{'HTTP_USER_AGENT'} = substr($ENV{'HTTP_USER_AGENT'}, 0, 200);
    $SENV{'HTTP_USER_AGENT'} =~ tr/<>"&/()'-/;
    if ($SENV{'SCRIPT_URI'}) {
        ($SENV{'SERVER_NAME'}, $SENV{'SCRIPT_PATH'}) = (split /\//, $SENV{'SCRIPT_URI'}, 4)[2,3];
        $SENV{'SCRIPT_PATH'} = "/$SENV{'SCRIPT_PATH'}";
    } else {
        $SENV{'SCRIPT_PATH'} = $ENV{'SCRIPT_NAME'};
        $SENV{'SERVER_NAME'} = $ENV{'SERVER_NAME'};
        $SENV{'SCRIPT_URI'}  = "http://$SENV{'SERVER_NAME'}$SENV{'SCRIPT_PATH'}";
    }
    $SENV{'SCRIPT_NAME'} = $1 if ($ENV{'SCRIPT_NAME'} =~ /([^\\\/]+$)/);
    $SENV{'REMOTE_ADDR'} = $ENV{'REMOTE_ADDR'};
    if ($SENV{'REMOTE_HOST'} eq $SENV{'REMOTE_ADDR'} || !$SENV{'REMOTE_HOST'}) {
        $SENV{'REMOTE_HOST'} = gethostbyaddr(pack('C4',split(/\./, $SENV{'REMOTE_ADDR'})),2);
        $SENV{'REMOTE_HOST'} = $SENV{'REMOTE_ADDR'} if (!$SENV{'REMOTE_HOST'});
    }

    #  PC/iMODE/J-SKYの判別(UAは騙りが可能なため、IPとリモホでも判別)
    if ($SENV{'HTTP_USER_AGENT'} =~ /^DoCoMo/ &&
       ($SENV{'REMOTE_HOST'} =~ /\.docomo\.ne\.jp$/ || $SENV{'REMOTE_ADDR'} =~ /^(210\.153\.84|210\.136\.161|203\.138\.45)/)) {
        $USER_AGENT = "iMODE";
    } elsif ($SENV{'HTTP_USER_AGENT'} =~ /^J-PHONE/ && 
       ($SENV{'REMOTE_HOST'} =~ /\.jp-[chknqrst]\.ne\.jp/ || $SENV{'REMOE_ADDR'} =~ /^(211\.8\.159|211\.8\.49|210\.134\.83|210\.146\.60|210\.169\.193|211\.127\.183)/)) {
        $USER_AGENT = "J-SKY";
    } else {
        $USER_AGENT = "OTHER";
    }
    #$SENV{'HTTP_USER_AGENT'}=$ENV{'HTTP_USER_AGENT'}="DoCoMo/1.0/P209is/c10";$USER_AGENT="iMODE"; #  for debug.

}
# </各種設定・初期化>



    # <セキュリティーチェック>

        #  最大バイト数チェック
        if ($stdio::max_byte < $ENV{'CONTENT_LENGTH'}) {
            Show_ErrorPage('[003]標準入力データサイズ超過',
                           'データが大きすぎます',
                           "<p>　送信されたデータのサイズが既定のサイズを超過したため、処理を中断しました。送信データのサイズを小さくして再試行してください。</p>");
        }

        #  フォームデータの有無チェック
        if (!@FORM_DATA) {
            Show_ErrorPage('[004]標準入力データなし',
                           'データがありません',
                           "<p>　リクエストされたデータに内容がありません。このシステムは直接起動することはできません。正規のフォームから再送信してください。</p>");
        }

        #  メソッドチェック(POSTメソッド未対応機種があるJ-PHONEはチェック対象外)
        if ($USER_AGENT ne "J-SKY" && $SYS{'rmethod'} eq "POST" && $ENV{'REQUEST_METHOD'} ne "POST") {
            Show_ErrorPage('不正な要求メソッド',
                           '要求メソッドが不正です',
                           "<p>　要求(リクエスト)メソッドが&quot;POST&quot;以外で呼び出されました。このシステムはセキュリティー保護のため、&quot;POST&quot;メソッド以外での呼び出しは許可しておりません。</p>");
        }

        #  参照元チェック(REFERERを吐かない携帯電話はチェック対象外)
        if ($USER_AGENT eq "OTHER" && $INI{'SetUrl'} && ($SENV{'HTTP_REFERER'} !~ /$INI{'SetUrl'}/i || $SENV{'HTTP_REFERER'} !~ /$SENV{'SCRIPT_URI'}/)) {
            Show_ErrorPage('[005]不正な参照元',
                           '参照元の値が不正です',
                           "<p>　環境変数&quot;HTTP_REFERER&quot;(参照元)の値が不正(未検出、もしくは他のサイトのURLを検出)です。このシステムはセキュリティー保護のため、所定のページ以外からの参照(直接アクセス)は許可しておりません。恐れ入りますが、正規のフォームから再送信してください。</p>"
                         . "<p>　環境変数を改変するアプリケーション(個人用のプロクシサーバーやファイアウォールソフト等も含まれます)を使用されている場合は、このエラーの原因となっている可\能性がありますので、一時的に外して再送信してください。ご不便をおかけして申し訳ありません。</p>\n"#);
                         );
        }

    # </セキュリティーチェック>


    # <タイムアウトのセッション解放・添付一時ファイルを削除 />
    if (opendir DIR, $SYS{'TempDir'}) {
        my($dir_size) = 0;
        while ($_ = readdir DIR) {
            if ((/\.ses$/ || /\.tmp$/) && (-M "$SYS{'TempDir'}$_") * 86400 > 900) {
                unlink "$SYS{'TempDir'}$_";
            } else {
                $dir_size += (-s "$SYS{'TempDir'}$_");
            }
        }
        closedir DIR;

        #  サーバー側に一時保存するデータが既定のサイズ内がチェック
        if ($max_buff && $max_buff < $dir_size) {
            Show_ErrorPage('[006]バッファサイズオーバー',
                           '時間をおいて再送信してください',
                           "<p>　ただいまサーバー側の既定バッファサイズを超過している状態のため、処理を継続できません。恐れ入りますが、時間をおいて再試行してください。ご不便をおかけして申し訳ありません。</p>\n");
        }
    }

    # <セッションID/フォームIDの取得 => セッション情報を読み出す />
    if ($STDIO{'_SESSION-ID'} =~ /^[0-9A-F]{16}-(\w+)$/) {
        my(%flag, $ses_file);

        $FORM_ID = $1;
        $SESSION_ID   = $STDIO{'_SESSION-ID'};
        $SESSION_FILE = "$SYS{'TempDir'}$SESSION_ID.ses";

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";

        #  送信完了フラッグの確認 (二度送信防止) => 指定URLへジャンプ or 送信完了ページ表示 => 終了
        if (stdio::getSession($ses_file, \%flag, $SESSION_ID)) {
            if ($flag{'redirect'} ne "") {
                print "Location: $flag{'redirect'}\n"
                    . "\n";
            } else {
                &Show_SubmittedPage;
            }
            exit;
        }

        #  セッションファイル開く or タイムアウト
        if (!open IN, $SESSION_FILE) {
            Show_ErrorPage('[007]セッションアウト',
                           'このセッションは無効です',
                           "<p>　有効なセッション情報を読み出すことができませんでした。原因として以下のことが考えられます。もし送信の作業途中であった場合、これまでの送信内容は失われました。恐れ入りますが、最初からやり直してください。ご不便をおかけして申し訳ありません。</p>\n"
                         . "<ul>\n"
                         . "  <li>データの送信がないまま、一定時間が経過した。</li>\n"
                         . "  <li>送信後にブラウザの[戻る]で戻って再送信しようとした。</li>\n"
                         . "  <li>送信後にリロード(再読込)を行った。</li>\n"
                         . "</ul>\n");
        }
        @session = <IN>;
        close IN;

    # <セッションIDが無いor値が不正 => セッションID/フォームIDの設定 />
    } else {
        $FORM_ID = substr $STDIO{'_FORM-ID'}, 0, 20;
        $FORM_ID =~ tr/A-Za-z0-9_//cd;  #  セキュリティーガード
        $FORM_ID = 'DEFAULT' if ($FORM_ID eq "");
        $SESSION_ID   = sprintf("%02X%02X%02X%02X%X", (split /\./, $ENV{'REMOTE_ADDR'})[0..3], time) . "-$FORM_ID";
        $SESSION_FILE = $SYS{'TempDir'} . "$SESSION_ID.ses";
    }

    # <ページIDの設定>
    if ($STDIO{'_FORM-PAGE'} eq "") {
        $PAGE_ID = "<DEFAULT>";
    } else {
        $PAGE_ID = substr $STDIO{'_FORM-PAGE'}, 0, 40;
        $PAGE_ID =~ tr/A-Za-z0-9_.\-//cd;  #  セキュリティーガード
    }

#  コマンドファイル名の設定
$command_file = $STDIO{'_COMMAND-FILE'};
undef $command_file if ($command_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # セキュリティーガード


#  コマンドファイルを読み込む
if (open IN, "$command_file") {
    my($data, $data2, $flag, $flag2);
    read IN, $data, (-s $command_file);
    close IN;

    $data =~ s/<!--(.|\s)*-->//g;
    $data =~ s/\r\n|\r/\n/g;
    foreach (split /\n/, $data) {
        if ($flag) {
            if (/^<\//) {
                $STDIO{$key} = $data2;
                push @FORM_DATA, $key;
                $flag = $flag2 = 0;
                $key = $data2 = "";
            } else {
                if ($STDIO{$key} && !$flag2) {
					$STDIO{$key} .= "\t";
					$flag2 = 1;
				}
				$data2 .= "$_\n";
                $STDIO{$key} .= "$_\n";
            }
        } elsif (/^<([^>]+)>([^<]*)<\//) {
            my($key, $val) = ($1, $2);
            push @FORM_DATA, $key;
            if (!$STDIO{$key}) {
				$STDIO{$key} = $val;
			} else {
            	$STDIO{$key} .= "\t$val";
            }
        } elsif (/^<([^>]+)>/) {
            $key = $1;
            $flag = 1;
        }
    }
}

#  コマンド読み込み
&Read_Command;

# <置換キーの設定>
%key_name = (
    'CODE'    => '送信番号',
    'TIME'    => '送信時間',
    'HOST'    => 'リモートホスト',
    'ADDR'    => 'リモートアドレス',
    'AGENT'   => 'エージェント',
    'NAME'    => '名前',
    'MAIL'    => 'メールアドレス',
    '_SUBJECT' => '件名'
);

#  既定入力名/既定初期値
$type{'MAIL'} = $type{'_TO'} = $type{'_REPLY-TO'} = 'MAIL';
$type{'CC'} = $type{'_BCC'} = 'MAIL2';
$type{'NAME'} = $type{'_SUBJECT'} = $type{'_SUBJECT2'} = 'TEXT';
$maxval{'NAME'}     = 256 if ($maxval{'NAME'} > 256);
$maxval{'_SUBJECT'} = 256 if ($maxval{'_SUBJECT'} > 256);
$maxval{'_SUBJECT2'}= 256 if ($maxval{'_SUBJECT2'} > 256);
$NOBLANK{'MAIL'} = 1 if ($STDIO{'_CCOPY'});


#  確認ページからの送信では無い
if (!$STDIO{'__SUBMIT__'}) {

    #  フォームデータチェック
    ($err_msg, @list) = &Check_FormData;

    # <入力不備がある場合>
    if ($err_msg) {
        my($form_page) = $STDIO{'_FORM-PAGE'};

        #  ケータイの場合 => B要素排除 全角カナ半角変換
        if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $err_msg =~ s/<\/?b>//g;
            jcode::z2h_sjis(\$err_msg);
        }

        #  添付ファイル削除
        unlink @stdio::file if (@stdio::file);

        #  エラーメッセージをUL要素による箇条書き
        $err_msg = "<ul>\n"
                 . $err_msg
                 . "</ul>";

        # <フォームページのHTML解析 既入力状態で表示>
        undef $form_page if ($form_page =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # セキュリティーガード
        if (open IN, $form_page) {
            my(@element, $data, $next_file, $hidden1, $hidden2, %i);
            my($i) = 0;

            read IN, $data, (-s $form_page);
            close IN;

            $next_file = (split /\t/, $STDIO{'_NEXT'}, 2)[0];
            $hidden1 = qq|<input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />|;
            $hidden2 = qq|<input type="hidden" name="_FORM-PAGE" value="$STDIO{'_FORM-PAGE'}" />|;
            undef $next_file if ($next_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # セキュリティーガード

            $data =~ s/<!--\/COMMENT-->/-->/gi;
            $data =~ s/<!--COMMENT-->/<!--/gi;
            $data =~ s/<!--PRINT//gi;
            $data =~ s/PRINT-->//gi;
            $data =~ s/<!--ERROR MESSAGE-->/$err_msg/;
            $data =~ s/<!--#[^>]+>//g;  #  セキュリティーガード(SSIコマンド削除)

            if (-f $SESSION_FILE) {
                $data =~ s/(<form\s+[^>]+>)/Check_FormAction($1,$hidden1)/egi;
            }
            if ($data !~ /name=["']?_FORM-PAGE["']?/i && $next_file) {
                $data =~ s/(<form\s+[^>]+>)/Check_FormAction($1,$hidden2)/egi;
            }

            #  フォーム送信先をチェック
            sub Check_FormAction #($form_tag, $hidden)
            {
                my($form_tag, $hidden) = @_;
                #return $_[0] =~ /$SENV{'SCRIPT_NAME'}/ ? "$data$_[1]" : $_[0];
                return $form_tag =~ /$SENV{'SCRIPT_NAME'}/ ? "$form_tag$hidden" : $form_tag;
            }

            @element = split(/(<[^>]*>)/, $data);
            undef $data;

            foreach (@element) {
                my($name, $value);

                if (/^<input|select|option|textarea/i) {

                    #  入力タイプ取得
                    if (/^<\/select/i) {
                        $select_name = "";
                    } elsif (/^<\//) {
                        $data .= $_;
                        $i ++;
                        next;
                    } elsif (/^<select/i) {
                        $multiple = / multiple/i ? 1 : 0;
                        $type = "select";
                    } elsif (/^<option/i) {
                        $type = "option";
                    } elsif (/^<textarea/i) {
                        $type = "textarea";
                    } elsif (/ type=['"]?(\w+)['"]?/i) {
                        $type = $1 ne "" ? $1 : "text";
                    }
                    $type =~ tr/A-Z/a-z/;

                    #  image file hidden submit reset buttonの場合は無視
                    if ($type eq "hidden" || $type eq "submit" || $type eq "reset" ||
                        $type eq "button" || $type eq "file" || $type eq "image") {
                        $data .= $_;
                        $i ++;
                        next;
                    }

                    #  checked/selected属性を解除
                    s/ checked(=['"]?checked['"]?)?//g;
                    s/ selected(=['"]?selected['"]?)?//g;
                    s/ *\/>/>/g;  #  for XHTML

                    #  入力名取得
                    if ($type eq "option") {
                        $name = $select_name;
                    } else {
                        $name = $1 if (/ name=([^ >]*)/i);
                        $name =~ s/^["']//g;
                        $name =~ s/["']$//g;
                        $i{$name} = !defined $i{$name} ? 0 : $i{$name} + 1;
                        if ($type eq "select") {
                            $select_name = $name;
                            $data .= $_;
                            $i ++;
                            next;
                        }
                    }

                    #  値を取得
                    $value = $1 if (/ value=([^ >]*)/i);
                    $value =~ s/^["']//g;
                    $value =~ s/["']$//g;
                    if ($type eq "textarea" || ($type eq "option" && $value eq "")) {
                        $value = $element[$i+1];
                    }

                    #  既入力値を初期値に設定
                    if ($type eq "text" || $type eq "password") {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        s/ value=[^ >]*//i;
                        s/>/ value="$value2">/i;
                    } elsif ($type eq "textarea") {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        $value2 =~ s/<br \/>/\n/g;
                        if ($element[$i+1] =~ /^(<\/textarea>)$/i) {
                            $element[$i+1] = "$value2$1";
                        } else {
                            $element[$i+1] = $value2;
                        }
                    } else {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        my($name2);
                        foreach (split /\t/, $STDIO{$name}) {
                            if ($_ eq $value) {
                                $name2 = $_;
                                last;
                            }
                        }
                        $name2 = $STDIO{$name} if (!defined $name2);
                        if ($type eq "checkbox" || $type eq "radio") {
                            if (($name2 eq $value && $value ne "") || ($type eq "checkbox" && $value eq "" && $name2 =~ /^ON$/i)) {
                                s/>/ checked="checked">/;
                            }

                        } elsif ($type eq "option") {
                            if ($multiple && $name2 eq $value) {
                                s/^<option/<option selected="selected"/i;
                            } elsif ($value eq $value2) {
                                s/^<option/<option selected="selected"/i;
                            }
                        }
                    }
                }
                $data .= $_;
                $i ++;
            }

            #  HTML出力開始
            print "Content-Type: text/html\n";
            print "Content-Length: " . length($data) . "\n";
            print "\n";

            print $data;
            exit;
        }
        # </フォームページのHTML解析 既入力状態で表示>

        $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
        $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
        $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
        $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css" />\n] if ($link_css);

        #  エラーメッセージだけを表示
        print "Content-Type: text/html", $CHARSET, "\n";
        print "\n";
        print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
$link_css<title>$title [入力不備]</title>
</head>
<body $body>

<h1>入力不備</h1>
<p>　フォームの入力内容に不備があります。もう一度確認のうえ再送信してください。</p>
$err_msg

</body>
</html>
_EOF_

        exit;

    }
    # </入力不備がある場合>


    #  添付ファイル等の重複送信対策開始
    Check_DuplicationSubmit("begin") if ($USER_AGENT !~ /^(iMODE|J-SKY)$/);

    #  ページIDを付与 => 重複データは上書き
    my($i) = 0;
    unshift @list, $PAGE_ID;
    foreach (@session) {
        if ((split /\t/, $_, 2)[0] eq $PAGE_ID) {
            last;
        }
        $i ++;
    }
    $session[$i] = join("\t", @list) . "\n";

}


#  次のページがある場合 or 送信前確認の場合
if (!$STDIO{'_SUBMIT'}) {

    #  セッションを保存
    if (!open OUT, ">$SESSION_FILE") {
        Show_ErrorPage('[008]ファイル書込エラー',
                       'セッションファイルの書き込みができません',
                       "<p>　セッションファイルの書き込みができません。セッションファイルへの書き込み用アクセス権が与えられていない可\能性があります。</p>");
    }
    print OUT @session;
    close OUT;

    #  セッション情報128KB超過 or 20個超過で異常と見なし強制終了 => セッション解放 => エラーメッセージ
    if ((-s $SESSION_FILE) > 131072 || $#session > 20) {
        unlink $SESSION_FILE;
        Show_ErrorPage('[009]パラメーターエラー');
    }

    #  確認ページ表示
    if ($STDIO{'_NEXT'} =~ /^confirm$/i || $STDIO{'_NEXT'} eq "") {
        &Show_ConfirmPage(*session);

    #  次ページへジャンプ
    } elsif ($STDIO{'_NEXT'} =~ /^http/) {
        print "Location: $STDIO{'_NEXT'}?$SESSION_ID\n"
            . "\n";

    #  次ページを表示
    } else {
        my($data, $next_file, $hidden);

        $next_file = $STDIO{'_NEXT'};
        undef $next_file if ($next_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # セキュリティーガード
        $hidden    = qq|<input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />|
                   . qq|<input type="hidden" name="_FORM-PAGE" value="$next_file" />|;

        if (!open IN, $next_file) {
            Show_ErrorPage('[010]ファイル読込エラー',
                           'ファイルの読み込みができません',
                           "<p>　フォームファイルの読み込みができません。フォームファイルが所定の場所に存在しない、フォームファイルの読み込み用アクセス権が与えられていない可\能性があります。</p>");
        }
        read IN, $data, (-s $next_file);
        close IN;
        $data =~ s/(<form\s+([^>]+)>)/$1$hidden/i;

        #  HTML表示開始
        print "Content-Type: text/html\n";
        print "Content-Length: " . length($data) . "\n";
        print "\n";

        print $data;

    }

    exit;
}


    if (!@session) {
        Show_ErrorPage('[007]セッションアウト',
                       'このセッションは無効です',
                       "<p>　有効なセッション情報を読み出すことができませんでした。原因として以下のことが考えられます。もし送信の作業途中であった場合、これまでの送信内容は失われました。恐れ入りますが、最初からやり直してください。ご不便をおかけして申し訳ありません。</p>\n"
                     . "<ul>\n"
                     . "  <li>データの送信がないまま、一定時間が経過した。</li>\n"
                     . "  <li>送信後にブラウザの[戻る]で戻って再送信しようとした。</li>\n"
                     . "  <li>送信後にリロード(再読込)を行った。</li>\n"
                     . "</ul>\n");
    }

    #  送信完了フラッグの確認 (二度送信防止)
    if (!$STDIO{'_SESSION-ID'}) {
        my(%flag, $id, $ses_file);

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";
        if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $id = "$FORM_ID.$SENV{'HTTP_USER_AGENT'}";
        } else {
            $id = "$FORM_ID.$SENV{'REMOTE_ADDR'}";
        }

        #  送信完了フラッグの確認 (二度送信防止) => 指定URLへジャンプ or 送信完了ページ表示 => 終了
        if (stdio::getSession($ses_file, \%flag, $SESSION_ID)) {
            if ($flag{'redirect'} ne "") {
                print "Location: $flag{'redirect'}\n"
                    . "\n";
            } else {
                &Show_SubmittedPage;
            }

            exit;
        }
    }

    &Submit_Email(*session);




#------------------------------------------------------------------------------
# ■ フォームデータをチェックする (Check_FormData)
#
#     呼出元 : 
#     引  数 : セッションID
#     戻り値 : エラーメッセージ, リスト
#------------------------------------------------------------------------------

sub Check_FormData #(void)
{

    #  ! 局所変数宣言
    my(
        $err_msg,   # エラーメッセージ
        @list,
        %flag,
        $i
    );


    foreach (@FORM_DATA) {
        my($key, $val) = ($_, $STDIO{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  2回目以降は同じキーはパス
        next if ($flag{$key});
        $flag{$key} = 1;

        $val =~ s/^\t//;

        #  最大文字数の設定
        $maxval{$key} = 2048 if ($type{$key} ne 'INT' && $type{$key} ne 'YEN' && !$maxval{$key} && !$STDIO{"$key->name"});

        #  全角英数字の半角変換
        if ($z2hset{$key}) {
            my($from) = q[０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ＋－／＝＿｜＊！？”’＃＄￥％＆＠：；＾，（）｛｝＜＞　];
            my($to)   = q[0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-/=_|*!?"'#$\%&@:;^,(){}<> ];
            jcode::tr(\$val, $from, $to);
        }

        # <型チェック>

            #  ファイル型サイズチェック
            if ($STDIO{"$key->name"}) {
                if (!$SYS{'UseMultipart'}) {
                    unlink $key;
                    $err_msg .= qq|  <li>ファイルの添付はできません。</li>\n|;

                } else {
                    my($file_name) = $STDIO{"$key->name"};

                    #  ファイル名が不正 or 64バイト超
                    if (($file_name =~ /[^\w\-\[\]\(\).]/ && $INI{'NoAttach'}) || length $STDIO{"$key->name"} > 64) {
                        my($suffix) = $1 if ($file_name =~ /(\.[A-Za-z0-9]+)$/);
                        $file_name  = $$ + time;
                        $file_name .= $suffix;
                    }

                    $i ++;
                    $file_name = "$i-$file_name";

                    #  ファイルサイズチェック
                    if ($maxval{$key} && $STDIO{"$_->size"} > $maxval{$key}) {
                        $err_msg .= qq|  <li>アップロード可能\な1個あたりのファイルサイズは| . stdio::setComma($maxval{$key}) . qq|バイトまでです。</li>\n|;
                        unlink $key;  #  添付ファイル削除
                    } elsif ($minval{$key} && $STDIO{"$_->size"} < $minval{$key}) {
                        $err_msg .= qq|  <li>アップロード可能\な1個あたりのファイルサイズは| . stdio::setComma($maxval{$key}) . qq|バイト以上です。</li>\n|;
                        unlink $key;  #  添付ファイル削除
                    } elsif (!$STDIO{"$_->size"}) {
                        $err_msg .= qq|  <li>ファイルの中身がありません。空ファイルのアップロードはできません。</li>\n|;
                        unlink $key;  #  添付ファイル削除

                    #  値は (>\tサーバー内のファイルパス\tファイル名\tユーザー側でのファイルパス\tファイ巣サイズ\tMIMEタイプ)
                    } else {
                        $val = qq(>\t$STDIO{$key}\t$file_name\t$STDIO{"$key->path"}\t$STDIO{"$key->size"}\t$STDIO{"$key->type"});
                    }
                }

            #  メールアドレス型チェック
            } elsif ($type{$key} eq "MAIL") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val && $val !~ /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>はメールアドレス形式になっていません。(半角で正しく入力してください)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ && ! /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>はメールアドレス形式になっていません。(半角で正しく入力してください)</li>\n|;
                            last;
                        }
                    }
                }

            #  複数個列記メールアドレス型チェック
            } elsif ($type{$key} eq "MAIL2") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val && $val !~ /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}(,[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6})*$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>はメールアドレス形式になっていません。(半角で正しく入力してください)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ && ! /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}(,[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6})*$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>はメールアドレス形式になっていません。(半角で正しく入力してください)</li>\n|;
                            last;
                        }
                    }
                }

            #  URL型チェック
            } elsif ($type{$key} eq "URL") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    $val = "" if ($val eq 'http://');
                    if ($val && $val !~ /^https?:\/\/[\w|\:\@\-]+\.[\w|\:\!\#\%\=\&\-\|\@\~\+\.\?\/]+$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>はURL形式になっていません。(半角で正しく入力してください)</li>\n|;
                    }
                } else {
                    my(@url);
                    foreach (split /\t/, $val) {
                        $_ = "" if ($_ eq 'http://');
                        if ($_ && ! /^https?:\/\/[\w|\:\@\-]+\.[\w|\:\!\#\%\=\&\-\|\@\~\+\.\?\/]+$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>はURL形式になっていません。(半角で正しく入力してください)</li>\n|;
                            last;
                        }
                        push @url, $_;
                    }
                    $val = join "\t", @url if (@url);
                }

            #  通貨型チェック
            } elsif ($type{$key} eq "YEN") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /\D/) {
                        $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                    } elsif ($val ne "") {
                        1 while $val =~ s/(.*\d)(\d\d\d)/$1,$2/;
                        $val .= "円";
                    }
                } else {
                    my(@yen);
                    foreach (split /\t/, $val) {
                        if (/\D/) {
                            $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                            last;
                        } elsif ($_ ne "") {
                            1 while s/(.*\d)(\d\d\d)/$1,$2/;
                            $_ .= "円";
                            push @yen, $_;
                        }
                    }
                    $val = join "\t", @yen if (@yen);
                }

            #  数字型チェック
            } elsif ($type{$key} eq "FIGURE") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /\D/) {
                        $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (/\D/) {
                            $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                            last;
                        }
                    }
                }

            #  整数型チェック
            } elsif ($type{$key} eq "INT") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val !~ /^-?\d+$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (! /^-?\d+$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>は半角数字で入力してください。</li>\n|;
                            last;
                        }
                    }
                }

            #  半角文字型チェック
            } elsif ($type{$key} eq "BYTE") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /[^\x20-\x7e]/) {
                        $err_msg .= qq|  <li><b>$key_name</b>は半角で入力してください。</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (/[^\x20-\x7e]/) {
                            $err_msg .= qq|  <li><b>$key_name</b>は半角で入力してください。</li>\n|;
                            last;
                        }
                    }
                }

            #  論理型チェック
            } elsif ($type{$key} eq "BOOLEAN") {
                $val =~ s/<br \/>//gi;
                $val =~ s/\t//g;
                $val = !$val || $val =~ /off|no|false/i ? 'いいえ' : 'はい';

            #  ノーマルテキスト型チェック
            } elsif ($type{$key} eq "TEXT") {
                $val =~ s/<br \/>//gi;
            }

        # </型チェック>


        #  必須項目の未入力チェック
        if ($NOBLANK{$key} && ($val eq "" || $val =~ /\t\t/ || $val =~ /\t$/)) {
            $err_msg .= qq|  <li><b>$key_name</b>は必須項目のため記入してください。</li>\n|;

        #  二度入力一致の確認
        } elsif ($chkset{$key} && !($val eq "" || $val =~ /\t\t/ || $val =~ /\t$/)) {
            my($flag);
            my($default) = (split /\t/, $val)[0];
            foreach (split /\t/, $val) {
                if ($default ne $_) {
                    $err_msg .= qq|  <li><b>$key_name</b>が確認のために再入力されたものと一致しません。</li>\n|;
                    $flag = 1;
                    last;
                }
            }
            if (!$flag) {
                $val = $default;
            }

        #  最大値/制限文字数超過/最大チェック可能数チェック
        } elsif ($maxval{$key}) {
            if ($type{$key} eq "INT" || $type{$key} eq "YEN") {
                if ($val !~ /\t/) {
                    if ($val > $maxval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>は$maxval{$key}以下の値を記入してください。</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ > $maxval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>は$maxval{$key}以下の値を記入してください。</li>\n|;
                            last;
                        }
                    }
                }
            } elsif ($type{$key} eq "DEFINE") {
                my($count) = $val =~ tr/\t/\t/;
                if ($maxval{$key} && $count >= $maxval{$key}) {
                    $err_msg .= qq|  <li><b>$key_name</b>で選択できるのは$maxval{$key}個までです。</li>\n|;
                }
            } else {
                if ($val !~ /\t/) {
                    my($length) = length $val;
                    if ($length > $maxval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>は$maxval{$key}バイト以内(全角でその半分)で記入してください。(現在 $lengthバイト)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        my($length) = length;
                        if ($length > $maxval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>は$maxval{$key}バイト以内(全角でその半分)で記入してください。(現在 $lengthバイト)</li>\n|;
                            last;
                        }
                    }
                }
            }

        #  最小値/指定文字数不足/最低チェック可能数チェック
        } elsif ($minval{$key}) {
            if ($type{$key} eq "INT" || $type{$key} eq "YEN") {
                if ($val !~ /\t/) {
                    if ($val < $minval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>は$minval{$key}以上の値を記入してください。</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ < $minval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>は$minval{$key}以上の値を記入してください。</li>\n|;
                            last;
                        }
                    }
                }
            } elsif ($type{$key} eq "DEFINE") {
                my($count) = $val =~ tr/\t/\t/;
                if ($minval{$key} && $count <= $minval{$key}) {
                    $err_msg .= qq|  <li><b>$key_name</b>で選択できるのは$minval{$key}個までです。</li>\n|;
                }
            } else {
                if ($val !~ /\t/) {
                    my($length) = length $val;
                    if ($length < $minval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>は$minval{$key}バイト以上(全角でその半分)を記入してください。(現在 $lengthバイト)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        my($length) = length;

                        if ($length < $minval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>は$minval{$key}バイト以上(全角でその半分)を記入してください。(現在 $lengthバイト)</li>\n|;
                            last;
                        }
                    }
                }
            }
        }

        #  エラーが無ければ
        if (!$err_msg) {
            #$val = $val_name{$val} if ($valset{$key});

            #  結合項目の結合
            $val =~ s/\t/$joinset{$key}/g if (defined $joinset{$key});

            #  セッション情報に含めないキーで無い => セッション情報を保存
            if ($key !~ /^_(SET:[A-Z0-9]+|NOBLANK|SESSION-ID|NEXT|FORM-ID|FORM-PAGE|MAX-[A-Z]+|MIN-[A-Z]+|JOIN\(.*\)|Z2HCONV|EQCHECK)$/) {
                $key =~ s/\t/&#9;/g;
                $val =~ s/\t/&#9;/g;
                push @list, "$key=>$val";
            }
        }
    }

    #  必須項目の未入力チェック(checkbox/select要素等のキーが送らない項目用)
    foreach(keys %NOBLANK) {
        if ($_ && !$flag{$_} && $STDIO{$_} eq "") {
            my($key_name)  = $key_name{$_} eq "" ? $_ : $key_name{$_};
            $err_msg .= qq|  <li><b>$key_name</b>は必須項目のため選択してください。</li>\n|;
        }
    }

    return $err_msg, @list;
}#


#------------------------------------------------------------------------------
# ■ 送信前確認ページ表示 (Show_ConfirmPage)
#
#     呼出元 : Show_MainPage, Show_ChatPage, Login_Chat, Show_LoginPage
#     引  数 : (セッションID, )
#     戻り値 : (終了)
#------------------------------------------------------------------------------

sub Show_ConfirmPage #(*data)
{

    #  →仮引数
    local(*data) = @_;

    #  ! 局所変数宣言
    my(
        @form_data,
        $title,
        $body,
        $confirm,
        %DATA,
        %hidden
    );


    #  配列からハッシュ
    @form_data = Array_to_Hash(\@data, \%DATA);

    #  確認ページで表示しない項目
    foreach (split /\t/, $DATA{'_HIDDEN'}) { $hidden{$_} = 1; }
    $hidden{'CODE'} = $hidden{'TIME'} = 1;

    #  確認ページのHTML構成開始
    foreach (@form_data) {
        my($key, $val) = ($_, $DATA{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  隠し項目でない?
        if (!$hidden{$_}) {
            if ($val =~ /^>\t/) {
                my($name, $path, $size) = (split /\t/, $val)[2..4];
                $val = "$path (" . stdio::setComma($size) . "バイト)";
            }
            $val =~ s/  /　/g;
            $val = '<span class="blank">(未入力)</span>' if ($val eq "");

            #  ケータイ向け
            if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
                $val =~ tr/\t/\n/;
                if ($key eq '_SPLIT') {
                    $confirm .= $val eq "" ? "\n\n" : "■ $val\n\n";
                } elsif ($key !~ /^_/) {
                    $confirm .= "[$key_name]\n"
                              . "$val\n\n";
                }

            #  パソコン向け
            } else {
                $val =~ s/\t/<br \/>/g;
                if ($key eq '_SPLIT') {
                    $val = '　' if ($val eq "");
                    $confirm .= qq|  </table>\n|
                             .  qq|    <h2>$val</h2>\n|
                             .  qq|  <table border="0" cellpadding="5" width="80%" id="AutoNumber1" cellspacing="1">\n|;

                } elsif ($key =~ /^(NAME|MAIL|_SUBJECT)$/ || $key !~ /^_/) {
                    $confirm .= qq|    <tr>\n|
                             .  qq|      <th nowrap="nowrap" bgcolor="$INI{'BG-COLOR1'}" width="30%"><div class="bg_blue">$key_name</div></th>\n|
                             .  qq|      <td bgcolor="$INI{'BG-COLOR2'}" width="70%"><kbd>$val</kbd></td>\n|
                             .  qq|    </tr>\n|;
                }
            }
        }
    }

    $header= $DATA{'_PAGE-HEADER'} eq "" ? $INI{'header'} : $DATA{'_PAGE-HEADER'};
    $footer= $DATA{'_PAGE-FOOTER'} eq "" ? $INI{'footer'} : $DATA{'_PAGE-FOOTER'};
    $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
    $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
    $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
    $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css" />\n] if ($link_css);

    #  HTML表示開始 for ケータイ
    if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
        my($data);
        my($method) = ($SYS{'rmethod'} eq "GET" || $USER_AGENT eq "J-SKY") ? "GET" : "POST";

        jcode::z2h_sjis(\$confirm);
        $data = <<_EOF_;

<html lang="ja">
<head>
<title>$title [送信内容確認]</title>
</head>
<body $body>
<h1>■送信内容確認</h1>
<pre>
$confirm
</pre>
<form action="$SENV{'SCRIPT_NAME'}" method="$method">
  <input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />
  <div align="center">
    <input type="submit" name="_SUBMIT" value="送信" />
  </div>
</form>
</body>
</html>
_EOF_

        print "Content-Type: text/html\n";
        print "Content-Length: " , length($data), "\n";
        print "\n";
        print $data;
        #  --


    #  HTML表示開始 for PC
    } else {
        print "Content-Type: text/html", $CHARSET, "\n";
        print "\n";
        print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=shift_jis" />
<title>フリーライター椎名前太へのお問い合わせ</title>
<meta name="Keywords" content="住宅,フリーライター,椎名前太" />
<meta name="Description" content="住宅・モノ選びコンサルタント＆フリーライター椎名前太へのお問い合わせ" />
<meta name="robots" content="index,follow" />
<link href="https://secure1846.sakura.ne.jp/zenta1.com/css/contact_import.css" rel="stylesheet" type="text/css" />
</head>
<body>
<a name="top" id="top"></a>
<div id="structure">

<h1><img src="../img/contact/logo.jpg" alt="フリーライター椎名前太" /></h1>
<h2>住宅フリーライター椎名前太【主要コンテンツ】</h2>

<!--グローバルナビゲーション -->

<ul id="navi">
<li id="contact"><span class="pop"><a href="https://secure1846.sakura.ne.jp/zenta1.com/contact/contact.html" class="popup"><img src="../img/contact/navi/contact.jpg"/><img src="../img/contact/navi/contact_voice.jpg" class="large"/></a></span></li>
<li id="case"><span class="pop"><a href="http://www.zenta1.com/img/works/sample.pdf" target="_blank" class="popup"><img src="../img/contact/navi/case.jpg"/><img src="../img/contact/navi/case_voice.jpg" class="large"/></a></span></li>
<li id="works"><span class="pop"><a href="http://www.zenta1.com/works.html" class="popup"><img src="../img/contact/navi/works.jpg"/><img src="../img/contact/navi/works_voice.jpg" class="large"/></a></span></li>
<li id="profile"><span class="pop"><a href="http://www.zenta1.com/profile.html" class="popup"><img src="../img/contact/navi/profile.jpg" /><img src="../img/contact/navi/profile_voice.jpg" class="large"/></a></span></li>
</ul>



<!--コンテンツはここから　container開始 -->
<div id="contents">

<!-- 左側 -->
<div id="left_side">

<a href="http://aqua-d.biz/zenta/index.html"><img src="../img/common/bt_toppage.gif" alt="「フリーライター椎名前太」のトップページへ戻る" width="200" height="22" /></a>

<!-- ブログ -->
<div id="blog_link02">
<div id="blog_link">
<p>
<a href="http://menchi-da.blog.so-net.ne.jp/" target="_blank">月間アクセス<br />
<strong>７００００</strong>オーバー！<br />
<strong>「フリーライター前太のこだわりハウスメーカー比較」</strong> </a><br />
街の工務店から大手ハウスメーカーまで20社以上を
こだわり比較。その一部始終を公開します！</p>
</div>
</div>

<!-- ワークシート -->
<div id="worksheet_link">
<p>
<a href="https://secure1846.sakura.ne.jp/zenta1.com/worksheet/worksheet.html"><span class="or">無料でゲット！</span><br />
<strong>あなたの『心の底から納得できる家』が簡単にわかる
７枚のワークシート</strong></a>はこちらから↓<br />
<a href="https://secure1846.sakura.ne.jp/zenta1.com/worksheet/worksheet.html"><img src="../img/common/get_free.jpg" alt="無料でゲット" /></a></p>
</div>
</div>
<!-- 左側ここまで -->


<!--右側記事 -->
<div id="kiji">

<div id="contact">
<h2>フリーライター椎名前太へのお問い合わせ</h2>

<p id="step">お客様情報入力……<strong>内容確認画面</strong>……お問い合わせ完了</p>

<table border="0" cellpadding="7" width="80%" cellspacing="1">
$confirm
</table>

<form action="$SENV{'SCRIPT_NAME'}" method="$SYS{'rmethod'}">
  <input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />
  <hr size="1" />
  <div align="center" class="button">
    <input type="submit" name="_SUBMIT" value="　　送　信　　" /><input type="button" value="　　訂　正　　" onClick="history.back()" /><br />
    <font size="1">反応が遅い場合がありますが、送信ボタンは一度だけ押してしばらくお待ち下さい。</font>
  </div>
  <hr size="1" />
</form>
$footer

</div>
<div id="toppage"><a href="#top">▲ PAGE TOP</a></div>
</div>

</div>
<!--右側記事終了 -->

<!--　コピーライト -->
<div id="copyrignt">Copyright&copy;2009 Zenta Shiina. All Rights Reserved. </div>

</div>
<!--　structure終了 -->

</body>
</html>

_EOF_
    }

    exit;
}#


#------------------------------------------------------------------------------
# ■ 本送信後の処理 (Submit_Email)
#
#     呼出元 : main
#     引  数 : (*データ配列)
#     戻り値 : (終了)
#------------------------------------------------------------------------------

sub Submit_Email #(*data)
{

    #  →仮引数
    local(*data) = @_;

    #  ! 局所変数宣言
    my(
        %DATA,
        $space,         # キーと値の区切り
        $from,          # 管理者宛メールの差出人
        $title,         # 送信完了ページのタイトル(TITLE要素内容)
        $body,          # 送信完了ページのBODY要素の属性
        $link_css,      # 送信完了ページのCSSファイルへのLINK要素
        $mailbody1,     # メール本文(管理者に送信されるもの)
        $mailbody2,     # メール本文(送信者に送信されるもの)
        $time,          # 添付ファイル名に付けるUTC時間のシリアル値
        @form_data,
        %hidden         # 送信者宛メールで省略するキー名
    );


    #  配列からハッシュ
    @form_data = Array_to_Hash(\@data, \%DATA);

    #  キーと値の区切り (改行 or 空白)
    $space = $DATA{'_TYPE'} ? "\n" : " ";

    $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
    $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
    $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
    $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css">\n] if ($link_css);

    $time = time . "-";
    $DATA{'CODE'} = time . int(rand(10));
    $DATA{'TIME'} = scalar gmtime(time + $INI{'TimeZone'} * 3600);
    $DATA{'HOST'} = $SENV{'REMOTE_HOST'};
    $DATA{'ADDR'} = $SENV{'REMOTE_ADDR'};
    $DATA{'AGENT'}= $SENV{'HTTP_USER_AGENT'};

    #  CCメール本文に明記しない項目
    foreach (split /\t/, $DATA{'_HIDDEN2'}) { $hidden{$_} = 1; }

    # <メール本文作成開始>
    foreach (@form_data) {
        my($key, $val) = ($_, $DATA{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  添付ファイルの場合(">"で始まる) 書式 : (>\tサーバー内のファイルパス\tファイル名\tユーザー側でのファイルパス\tファイルサイズ\tMIMEタイプ)
        if ($val =~ /^>\t/) {
            my($fname, $name, $path, $size) = (split /\t/, $val)[1..4];
            $name = "$DATA{'_CODE'}$name";

            #  整形済みファイル名に変更 => パスを @attach_file1 に格納
            if (rename $fname, "$SYS{'TempDir'}$name") {
                push @attach_files1, "$SYS{'TempDir'}$name";
            }

            #  メール送信しない(サーバー側に保存する)場合
            if ($INI{'NoAttach'} && $SYS{'DataDirURI'}) {
                $val = "$path (" . stdio::setComma($size) . "バイト)\n"
                     . qq[$SYS{'DataDirURI'}$time$name\n];

            } else {
                $val = "$path (" . stdio::setComma($size) . "バイト)";
            }

        #  通常テキスト情報の場合
        } else {
            $val =~ s/\t/$space/g;
        }
        $val = '(未入力)' if ($key ne '_SPLIT' && $val eq "");

        #  データからメール本文を作成
        if ($key eq '_SPLIT') {
            $mailbody1 .= $val eq "" ? "\n\n" : "■ $val\n\n";
            $mailbody2 .= $val eq "" ? "\n\n" : "■ $val\n\n" if (!$hidden{$_} && $DATA{'_CCOPY'});
        } elsif ($key !~ /^_/) {
            $mailbody1 .= "[$key_name]$space"
                        . "$val\n\n";
            $mailbody2 .= "[$key_name]$space"
                        . "$val\n\n" if (!$hidden{$_} && $DATA{'_CCOPY'});
        }
    }
    # </メール本文作成開始>


    # <管理者宛メール送信>
    {

        $DATA{'_HEADER'} .= "\n" if ($DATA{'_HEADER'});
        $mailbody1 =<<_EOF_;
$DATA{'_HEADER'}
$mailbody1
$DATA{'_FOOTER'}

■ 送信時の情報 -----------------------------------------------------

 送信日時     : @{[scalar(gmtime(time + 3600 * $INI{'TimeZone'}))]}
 送信番号     : $DATA{'CODE'}

 サーバー名   : $SENV{'SERVER_NAME'} : $ENV{'SERVER_PORT'}
 スクリプト名 : $SENV{'SCRIPT_PATH'}
 要求メソ\ッド : $ENV{'REQUEST_METHOD'}
 参照元       : $SENV{'HTTP_REFERER'}
 エージェント : $SENV{'HTTP_USER_AGENT'}
 ホスト名(IP) : $SENV{'REMOTE_HOST'} ($SENV{'REMOTE_ADDR'})

---------------------------------------------------------------------
_EOF_

        #  HTML用の実体参照を実態に置換
        $mailbody1 =~ s/<br \/>/\n/g;
        $mailbody1 =~ s/&lt;/</g;
        $mailbody1 =~ s/&gt;/>/g;
        $mailbody1 =~ s/&quot;/"/g;
        $mailbody1 =~ s/&amp;/&/g;


        #  ヘッダの設定
        $DATA{'_SUBJECT'} = '(無題)' if ($DATA{'_SUBJECT'} eq "");
        $DATA{'_SUBJECT2'} = $DATA{'_SUBJECT'} if ($DATA{'_SUBJECT2'} eq "");
        $DATA{'MAIL'} = 'anonymous@on.the.net' if ($DATA{'MAIL'} eq "");
        if ($DATA{'NAME'} !~ /^[\s　]*$/) {
            $from = "$DATA{'NAME'} <$DATA{'MAIL'}>";
        } else {
            $from = $DATA{'MAIL'};
        }
        $INI{'mailto'} = $DATA{'_TO'} if (!$INI{'mailto'});

        #  管理者宛メールヘッダー
        %header1 = (
            "To"         => $INI{'mailto'},
            "From"       => $from,
            "Subject"    => $DATA{'_SUBJECT'},
            "X-Mailer"   => $VERSION,
            "X-MailID"   => $DATA{'CODE'}
        );
        $header1{'X-Priority'} = $DATA{'_PRIORITY'} if ($DATA{'_PRIORITY'} =~ /^[1-5]$/);
        $header1{'Bcc'} = $DATA{'_BCC'};
        $header1{'Cc'}  = $DATA{'_CC'};


        {
            my(@attach_files, $encode);

            $encode = $DATA{'_ENCODE'};
            foreach (@attach_files1) {
                my($file_name, $new_file, $mime_type);

                $mime_type = Get_MimeType($_);
                $file_name = $1 if (/([^\\\/]+)$/);
                $new_file  = "$SYS{'DataDir'}$time$file_name";
                $file_name =~ s/^\d+-//;
                if ($INI{'NoAttach'}) {
                    rename $_, $new_file;
                } else {
                    push @attach_files, "$_;$mime_type;$file_name";
                }
            }

            #  実際にメール送信
            if (!stdio::sendmail(\%header1, $mailbody1, 0, $encode, @attach_files)) {
                Show_ErrorPage('[012]メール送信エラー',
                               'メールの送信ができません',
                               "<p>　メールの送信ができません。メール送信プログラム[sendmail]へのパスが正しく設定されていない、実行アクセス権が与えられていない可\能性があります。</p>");

           }
        }
    }
    # </管理者宛メール送信>


    # <送信者宛メール送信>
    if ($DATA{'_CCOPY'}) {
        my(@attach_files2, $encode);

        $encode = $DATA{'_ENCODE2'} ? $DATA{'_ENCODE2'} : $DATA{'_ENCODE'};

        #  テンプレートファイルから読み込み
        if ($DATA{'_TEMPLATE'}) {
            $mailbody2 = $DATA{'_TEMPLATE'};
            $mailbody2 =~ s/{\$([^}]+)}/$DATA{$1}/g;

        #  通常のメール本文
        } else {
            $DATA{'_HEADER2'} .= "\n" if ($DATA{'_HEADER2'});
            $mailbody2 = <<_EOF_;
$DATA{'NAME'} 様

$DATA{'_HEADER2'}
$mailbody2
$DATA{'_FOOTER2'}
_EOF_

        }

        $mailbody2 =~ s/<br \/>/\n/g;
        $mailbody2 =~ s/&lt;/</g;
        $mailbody2 =~ s/&gt;/>/g;
        $mailbody2 =~ s/&quot;/"/g;
        $mailbody2 =~ s/&amp;/&/g;


        #  送信者宛メールヘッダー
        my(%header2) = (
            "To"         => $from,
            "From"       => $DATA{'_FROM'},
            "Subject"    => $DATA{'_SUBJECT2'},
            "X-Mailer"   => $VERSION,
            "X-MailID"   => $DATA{'CODE'}
        );
        $header2{'X-Priority'} = $DATA{'_PRIORITY2'} if ($DATA{'_PRIORITY2'} =~ /^[1-5]$/);
        $header2{'Reply-To'} = $DATA{'_REPLY'} if ($DATA{'_REPLY'});


        #  送信者宛添付ファイル
        foreach (split /\t/, $DATA{'_ATTACHMENT-FILE'}) {
            my($mime_type) = Get_MimeType($_);

            next if (/(^\/|\.\.\/|[^\w\-\.\/])/);  # セキュリティーガード
            push @attach_files2, "$SYS{'FileDir'}$_;$mime_type" if (-f "$SYS{'FileDir'}$_");
        }

        #  実際にメール送信
        if (!stdio::sendmail(\%header2, $mailbody2, 0, $encode, @attach_files2)) {
            Show_ErrorPage('[015]メール送信エラー',
                           'メールの送信ができません',
                           "<p>　メールの送信ができません。メール送信プログラム[sendmail]へのパスが正しく設定されていない、実行アクセス権が与えられていない可\能性があります。</p>");
        }
    }
    # </送信者宛メール送信>


    #  セッション解放
    unlink $SESSION_FILE;

    #  添付ファイル等の重複送信対策終了
    Check_DuplicationSubmit("free") if ($USER_AGENT !~ /^(iMODE|J-SKY)$/);

    #  添付ファイル削除
    unlink @attach_files1 if (@attach_files1);

    #  送信完了フラッグの確立 (二度送信防止)
    {
        my($id, %flag, $ses_file);

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";
        if ($STDIO{'_SESSION-ID'}) {
            $id = $SESSION_ID;
        } elsif ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $id = "$FORM_ID.$SENV{'HTTP_USER_AGENT'}";
        } else {
            $id = "$FORM_ID.$SENV{'REMOTE_ADDR'}";
        }
        $flag{'submited'} = 1;
        $flag{'redirect'} = $DATA{'_REDIRECT'} if ($DATA{'_REDIRECT'} ne "");
        stdio::setSession($ses_file, \%flag, $id, 600);
    }

    #  指定URLへジャンプ or 送信完了ページ表示 => 終了
    if ($DATA{'_REDIRECT'}) {
        print "Location: $DATA{'_REDIRECT'}\n"
            . "\n";

    } else {
        &Show_SubmittedPage;
    }

    exit;
}#


#------------------------------------------------------------------------------
# ■ 重複送信対策 (Check_DuplicationSubmit)
#
#     呼出元 : (汎用)
#     引  数 : (ファイル名)
#     戻り値 : (なし)
#------------------------------------------------------------------------------

sub Check_DuplicationSubmit
{

    #  →仮引数
    my($action) = @_;

    #  ! 局所変数宣言
    my($id, $ses_file, %ses);

    $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.check.ses";
    $id = $FORM_ID . $ENV{'REMOTE_ADDR'};

    if ($action eq "free") {
        stdio::setSession($ses_file, "", $id);
        return;
    }

    if (stdio::getSession($ses_file, \%ses, $id)) {
        if ($ses{'<SESSION-ID>'} && $ses{'<SESSION-ID>'} ne $SESSION_ID) {
            unlink "$SYS{'TempDir'}$ses{'<SESSION-ID>'}.ses";
            foreach (split /\t/, $ses{'<PAGE-ID>'}) {
                if (-f $ses{$_}) {
                    unlink $ses{$_};
                } else {
                    foreach (split /\t/, $ses{$_}) {
                        unlink $_;
                    }
                }
            }
            undef %ses;
        } elsif ($ses{$PAGE_ID} ne "") {
            if (-f $ses{$PAGE_ID}) {
                unlink $ses{$PAGE_ID};
            } else {
                foreach (split /\t/, $ses{$PAGE_ID}) {
                    unlink $_;
                }
            }
        }
    }
    $ses{'<SESSION-ID>'} = $SESSION_ID;
    $ses{'<PAGE-ID>'} .= "$PAGE_ID\t";
    $ses{$PAGE_ID} = join "\t", @afile if (@afile);
    stdio::setSession($ses_file, \%ses, $id);

    return;
}


#------------------------------------------------------------------------------
# ■ セッション保持用の配列をハッシュにする (Array_to_Hash)
#
#     呼出元 : Show_ConfirmPage Submit_Email
#     引  数 : (*データ配列, *データハッシュ)
#     戻り値 : (キーのリスト)
#------------------------------------------------------------------------------

sub Array_to_Hash #(*array, *hash)
{

    #  →仮引数
    local(*array, *hash) = @_;

    #  ! 局所変数宣言
    my(@key_list);

    foreach (@array) {
        chomp;
        my(@list) = split /\t/;
        shift @list;
        foreach (@list) {
            s/&#9;/\t/g;
            my($key, $val) = split /=>/, $_, 2;
            $hash{$key} = $val;
            push @key_list, $key;
        }
    }

    return @key_list;
}


#------------------------------------------------------------------------------
# ■ 拡張子からMimeTypeを取得する (Get_MimeType)
#
#     呼出元 : (汎用)
#     引  数 : (ファイル名)
#     戻り値 : (MimeType) 対応するものが無ければ 'application/octet-stream'
#------------------------------------------------------------------------------

sub Get_MimeType #($file)
{

    #  →仮引数
    my($file) = @_;

    #  ! 局所変数宣言
    my(%mime_type) = (
        'shtml' => 'text/html', 
        'stm'   => 'text/html',
        'hdml'  => 'text/hdml',
        'html'  => 'text/html',
        'htm'   => 'text/html',
        'xml'   => 'text/xml',
        'csv'   => 'text/plain',
        'txt'   => 'text/plain',
        'rtx'   => 'text/richtext',
        'css'   => 'text/css',
        'gif'   => 'image/gif',
        'jpeg'  => 'image/jpeg',
        'jpg'   => 'image/jpeg',
        'png'   => 'image/png',
        'bmp'   => 'image/bmp',
        'tiff'  => 'image/tiff',
        'tif'   => 'image/tiff',
        'ico'   => 'image/x-icon',
        'midi'  => 'audio/midi',
        'mid'   => 'addio/midi',
        'mp2'   => 'audio/mpeg',
        'mp3'   => 'audio/mpeg',
        'wav'   => 'audio/x-wav',
        'au'    => 'audio/basic',
        'zip'   => 'application/zip',
        'lzh'   => 'application/x-lzh',
        'lha'   => 'application/x-lzh',
        'swf'   => 'application/x-shockwave-flash',
        'js'    => 'application/x-javascript',
        'tar'   => 'application/x-tar',
        'gz'    => 'application/x-gzip',
        'pdf'   => 'application/pdf',
        'avi'   => 'video/x-msvideo',
        'mpeg'  => 'video/mpeg',
        'mpg'   => 'video/mpeg',
        'qt'    => 'video/quicktime',
        'mov'   => 'video/quicktime'
    );
    $file = $file =~ /\.(.+)$/ ? $1 : "";

    return defined $mime_type{$file} ? $mime_type{$file} : 'application/octet-stream';
}


#------------------------------------------------------------------------------
# ■ エラーページ表示 (Show_ErrorPage)
#
#     呼出元 : (汎用)
#     引  数 : (エラータイプ,エラータイトル,メッセージ)
#     戻り値 : (終了)
#------------------------------------------------------------------------------

sub Show_ErrorPage #($err_type, $err_title, $err_msg)
{

    #  →仮引数
    my($err_type, $err_title, $err_msg) = @_;

    $err_msg = $err_msg =~ /^<p>/i ? $err_msg : "<p>$err_msg</p>";

    #  レスポンスヘッダ出力 => HTML表示開始
    print "Content-Type: text/html", $CHARSET, "\n"
        . "Cache-Control: no-cache\n"
        . "Pragma: no-cache\n"
        . "\n";
    print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<base href="$SENV{'SCRIPT_URI'}" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<title>$INI{'Title'} [システムエラー]</title>
</head>
<body $INI{'Body'} class="ErrorPage">


<div class="error">
  <h2 class="error">&nbsp;<img border="0" src="$SENV{'SCRIPT_URI'}?[error]" alt="エラー" width="28" height="28" /> <font color="#FF0000">$err_title</font></h2>
  $err_msg
  <br />
  <br />
  <br />
  <div align="center" class="bar">
    <small><a href="javascript:history.back()">[←戻る]</a> <a href="javascript:location.reload(true)">[再試行]</a></small>
  </div>
  <p><small>※ エラーが解決しない場合は以下の情報を添えてこのサイトの管理者へご照会ください。</small></p>
  <pre class="error-info" style="color:gray; font-size:12px">
  $err_type ($VERSION)
  TIME  :@{[scalar gmtime(time+$INI{'TimeZone'}*3600)]} (GMT$INI{'TimeZone'})
  IPADDR:$SENV{'REMOTE_HOST'} ($ENV{'REMOTE_ADDR'})
  AGENT :$ENV{'HTTP_USER_AGENT'}
  REFFER:$ENV{'HTTP_REFERER'}</pre>
</div>

</body>
</html>
_EOF_

    exit;
}#


#------------------------------------------------------------------------------
# ■ CGI経由でファイル出力 (Show_File_by_CGI)
#
#     呼出元 : (汎用)
#     引  数 : 識別名
#     戻り値 : (終了)
#------------------------------------------------------------------------------

sub Show_File_by_CGI #($name)
{

    #  →仮引数
    my($name) = @_;

    #  ! 局所変数宣言
    my($data, $flag, $type);

    while (<DATA>) {
        next if (/^#/);
        if (!$flag) {
            my($name2);
            chomp;
            ($name2, $type) = split /,/;
            next if ($name eq "");
            $flag = $name eq $name2 ? 2 : 1;
        } elsif (/^__SEPARATOR__/) {
            last if ($flag == 2);
            $flag = 0;
        } elsif ($flag == 2) {
            $data .= $_;
        }
    }

    if ($data ne "") {
        $type = 'application/octet-stream' if ($type eq "");
        binmode STDOUT;
        if ($type =~ /^(image|audio|video)\//) {
            my(@data);
            $data =~ tr/A-Fa-f0-9\r\n\t //cd;
            @data = split /\s+/, $data;
            print "Content-Type: ", $type, "\n";
            print "Content-Length: ", scalar @data, "\n";
            print "\n";
            foreach (@data) {
                print pack('C*', hex $_);
            }
        } else {
            print "Content-Type: ", $type, "\n";
            print "Content-Length: ", length $data, "\n";
            print "\n";
            print $data;
        }
    } else {
        print "Content-Type: text/html\n"
            . "Status: 204 No Content\n"
            . "\n";
    }

    exit;
}#


#==============================================================================
# ● 送信完了ページ表示 (Show_SubmittedPage)
#==============================================================================

sub Show_SubmittedPage
{

    #  送信完了ページ表示
    print "Content-Type: text/html", $CHARSET, "\n";
    print "\n";
    print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
$link_css<title>$title [送信完了]</title>
</head>
<body $body>
<h1>送信完了</h1>

<p>　フォームのデータは正常に送信されました。</p>

</body>
</html>
_EOF_

    return;
}#



#==============================================================================
# ● コマンドを読み込み (Read_Command)
#==============================================================================

sub Read_Command
{

    #  ! 局所変数宣言
    my(%i);

    #  入力必須
    foreach (split /\t/, $STDIO{'_NOBLANK'}) {
        $NOBLANK{$_} = 1;
    }

    #  二度入力確認項目
    foreach (split /\t/, $STDIO{'_EQCHECK'}) {
        $chkset{$_}  = 1;
    }

    #  全角英数半角変換
    foreach (split /\t/, $STDIO{'_Z2HCONV'}) {
        $z2hset{$_}  = 1;
    }

    # <型定義>

        #  メールアドレス型
        foreach (split /\t/, $STDIO{'_SET:MAIL'}) {
            $type{$_} = "MAIL";
            $maxval{$_}  = 128;
        }

        #  複数列記メールアドレス型
        foreach (split /\t/, $STDIO{'_SET:MAIL2'}) {
            $type{$_} = "MAIL2";
            $maxval{$_}  = 256;
        }

        #  一行テキスト型
        foreach (split /\t/, $STDIO{'_SET:TEXT'}) {
            $type{$_} = "TEXT";
            $maxval{$_}  = 256;
        }

        #  URL(http)型
        foreach (split /\t/, $STDIO{'_SET:URL'}) {
            $type{$_} = "URL";
            $maxval{$_} = 128;
        }

        #  数字型(文字列としての)
        foreach (split /\t/, $STDIO{'_SET:DIGIT'}) {
            $type{$_} = "FIGURE";
            $maxval{$_} = 256;
        }

        #  半角(1バイト)型
        foreach (split /\t/, $STDIO{'_SET:BYTE'})  {
            $type{$_} = "BYTE";
            $maxval{$_} = 256;
        }

        #  通貨型(数値型)
        foreach (split /\t/, $STDIO{'_SET:YEN'}) {
            $type{$_} = "YEN";
            $maxval{$_} = 999999999999999;
            $minval{$_} = 0;
        }

        #  整数型(数値型)
        foreach (split /\t/, $STDIO{'_SET:INT'})  {
            $type{$_} = "INT";
            $maxval{$_} = 999999999999999;
            $minval{$_} = -999999999999999;
        }

        #  論理型(YES/NO型)
        foreach (split /\t/, $STDIO{'_SET:BOOLEAN'})  {
            $type{$_} = "BOOLEAN";
        }

        #  固定値型
        foreach (split /\t/, $STDIO{'_SET:DEFINE'}) {
            $type{$_} = "DEFINE";
        }

    # </型定義>

    #  ---
    foreach (@FORM_DATA) {
        $i{$_} = 0 if (!defined $i{$_});
        my($data) = $STDIO{$_} =~ /\t/ ? (split /\t/, $STDIO{$_})[$i{$_}++] : $STDIO{$_};

        #  最大値(バイト/値/チェック可能数)
        if (/^_MAX-VALUE\((\d{1,16})\)/) {
            my($max) = $1;
            if ($type{$_} eq "INT" || $type{$_} eq "YEN") {
                $maxval{$data} = $max if ($max >= -999999999999999 && $max <= 999999999999999);
            } elsif ($STDIO{"$_->name"}) {
                $maxval{$data} = $max;
            } else {
                $maxval{$data} = $max if ($max > 0 && $max <= 10240);
            }

        #  最小値(バイト/値/チェック可能数)
        } elsif (/^_MIN-VALUE\((\d{1,16})\)/) {
            my($min) = $1;
            if ($type{$_} eq "INT" || $type{$_} eq "YEN") {
                $minval{$data} = $min if ($min >= -999999999999999 && $min <= 999999999999999);
            } elsif ($STDIO{"$_->NAME"}) {
                $minval{$data} = $min;
            } else {
                $minval{$data} = $min if ($min > 0 && $min <= 10240);
            }

        #  結合項目
        } elsif (/^_JOIN\(([^\)]+)\)/) {
            $joinset{$1} = $data;

        #  添付ファイル
        } elsif ($STDIO{"$_->name"}) {
            push @afile, $STDIO{$_};
        }
    }

    return;
}

#  for Debug.

sub h #(void)
{

    print "Content-Type: text/html", $CHARSET, "\n"
        . "\n"
        . "<plaintext>\n";

}#

sub d #(@_)
{

    print "Content-Type: text/html", $CHARSET, "\n"
        . "\n"
        . "<plaintext>\n";
    print @_;

    exit;
}#


#******************************************************************************
# □ Show_File_by_CGI関数で出力するデータ
#
#   * "#"で始まる行はコメントと見なし処理の対象としない。
#   * クエリー文字列か引数で[識別名]を指定 (filename.cgi?[識別名])
#   * 書式 : (1行目=識別名,MIME-TYPE セパレータ行=__SEPARATOR__)
#******************************************************************************

__DATA__
error,image/gif
47 49 46 38 39 61 1c 00 1c 00 a1 00 00 00 00 00 ff 00 00 ff
ff ff bf bf bf 21 f9 04 01 00 00 03 00 2c 00 00 00 00 1c 00
1c 00 00 02 68 9c 8f a9 cb 18 1f 9a 4c 30 ce 59 df 95 d9 6e
d5 69 1f 15 8e 4e 28 9a 68 fa 65 82 90 a9 d5 1b b7 f3 0b 57
36 24 00 40 0e d9 b8 7a 3f 20 8b 31 f4 d1 74 9c 1b 11 57 43
3a 95 cb a0 94 87 a3 56 8f 87 e1 4b 6b f4 9c b0 b8 32 94 39
7e 98 c1 61 12 39 5b 2c 47 07 5e b3 3d ba ca 97 e8 fa be c6
0f 18 08 c8 27 88 32 50 00 00 3b
__SEPARATOR__
