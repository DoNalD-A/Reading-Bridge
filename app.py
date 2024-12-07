from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

# 휘발성 저장소 (서버 재시작 시 초기화됨)
ebooks = []


def initialize_data():
    """서버 시작 시 데이터를 초기화합니다."""
    global ebooks
    ebooks.clear()  # 기존 데이터를 완전히 비웁니다.


# 메인화면
@app.route('/')
@app.route('/home')
def home():
    global ebooks
    response = make_response(render_template('메인화면.html'))
    # 로컬스토리지를 초기화할 플래그를 클라이언트에 전달
    response.set_cookie('clearStorage', 'true')
    return response


@app.route('/mentoring')
def mentoring():
    return render_template('멘토링창.html')


@app.route('/ebook-list')
def ebook_list():
    return render_template('전자책 목록.html')


@app.route('/ebook-create', methods=['GET', 'POST'])
def ebook_create():
    global ebooks
    if request.method == 'POST':
        # JSON 데이터 수신
        data = request.json
        if not data.get('title'):
            return jsonify({'error': '제목이 필요합니다.'}), 400

        # 데이터 저장
        ebooks.append(data)
        return jsonify({'message': '전자책이 저장되었습니다!'}), 200

    return render_template('전자책2.html')


@app.route('/ebook-view/<title>')
def ebook_view(title):
    global ebooks
    # 제목과 일치하는 전자책 찾기
    ebook = next((book for book in ebooks if book['title'] == title), None)

    if ebook:
        return render_template('전자책2.html', ebook=ebook)
    else:
        return "해당 전자책을 찾을 수 없습니다.", 404


# 책들
@app.route('/books')
def books():
    return render_template('책들.html')


# 각각의 책 상세 페이지
@app.route('/book1')
def book1():
    return render_template('책 목록.html')


@app.route('/book2')
def book2():
    return render_template('책 목록2.html')


@app.route('/book3')
def book3():
    return render_template('책 목록3.html')


@app.route('/book4')
def book4():
    return render_template('책 목록4.html')


@app.route('/book5')
def book5():
    return render_template('책 목록5.html')


@app.route('/my')
def my():
    return render_template('my.html')


# 전자책 데이터 확인 (디버깅용)
@app.route('/ebooks', methods=['GET'])
def get_ebooks():
    global ebooks
    return jsonify(ebooks)


if __name__ == '__main__':
    initialize_data()  # 서버 시작 시 데이터를 완전히 초기화합니다.
    app.run(debug=True)
