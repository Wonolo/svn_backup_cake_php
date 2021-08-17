require 'gilded_rose'

shared_examples 'decrements sell_in' do |n|
  it "by #{n}" do
    expect { update_quality([item]) }.to change { item.sell_in }.by(-n)
  end
end

shared_examples 'decrements quality' do |n|
  it "by #{n}" do
    expect { update_quality([item]) }.to change { item.quality }.by(-n)
  end
end

shared_examples 'increments quality' do |n|
  it "by #{n}" do
    expect { update_quality([item]) }.to change { item.quality }.by(n)
  end
end

describe "#update_quality" do
  context "with a single" do
    let(:item) { Item.new(name, initial_sell_in, initial_quality) }

    let(:initial_sell_in) { 5 }
    let(:initial_quality) { 10 }

    context "normal item" do
      let(:name) { "NORMAL ITEM" }

      it_behaves_like 'decrements sell_in', 1

      context "before sell date" do
        it_behaves_like 'decrements sell_in', 1
      end

      context "on sell date" do
        let(:initial_sell_in) { 0 }
        it_behaves_like 'decrements quality', 2
      end

      context "after sell date" do
        let(:initial_sell_in) { -10 }
        it_behaves_like 'decrements quality', 2
      end

      context "of zero quality" do
        let(:initial_quality) { 0 }
        it_behaves_like 'decrements quality', 0
      end
    end

    context "Aged Brie" do
      let(:name) { "Aged Brie" }

      it_behaves_like 'decrements sell_in', 1

      context "before sell date" do
        it_behaves_like 'increments quality', 1

        context "with max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "on sell date" do
        let(:initial_sell_in) { 0 }

        it_behaves_like 'increments quality', 2

        context "near max quality" do
          let(:initial_quality) { 49 }
          it_behaves_like 'increments quality', 1
        end

        context "with max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "after sell date" do
        let(:initial_sell_in) { -10 }

        it_behaves_like 'increments quality', 2

        context "with max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end
    end

    context "Sulfuras" do
      let(:initial_quality) { 80 }
      let(:name) { "Sulfuras, Hand of Ragnaros" }

      it_behaves_like 'decrements sell_in', 0

      context "before sell date" do
        it_behaves_like 'decrements quality', 0
      end

      context "on sell date" do
        let(:initial_sell_in) { 0 }
        it_behaves_like 'decrements quality', 0
      end

      context "after sell date" do
        let(:initial_sell_in) { -10 }
        it_behaves_like 'decrements quality', 0
      end
    end

    context "Backstage pass" do
      let(:name) { "Backstage passes to a TAFKAL80ETC concert" }

      it_behaves_like 'decrements sell_in', 1

      context "long before sell date" do
        let(:initial_sell_in) { 11 }

        it_behaves_like 'increments quality', 1

        context "at max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "medium close to sell date (upper bound)" do
        let(:initial_sell_in) { 10 }

        it_behaves_like 'increments quality', 2

        context "at max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "medium close to sell date (lower bound)" do
        let(:initial_sell_in) { 6 }

        it_behaves_like 'increments quality', 2

        context "at max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "very close to sell date (upper bound)" do
        let(:initial_sell_in) { 5 }

        it_behaves_like 'increments quality', 3

        context "at max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "very close to sell date (lower bound)" do
        let(:initial_sell_in) { 1 }

        it_behaves_like 'increments quality', 3

        context "at max quality" do
          let(:initial_quality) { 50 }
          it_behaves_like 'increments quality', 0
        end
      end

      context "on sell date" do
        let(:initial_sell_in) { 0 }

        it 'has 0 quality' do
          update_quality([item])
          expect(item.quality).to eq(0)
        end
      end

      context "after sell date" do
        let(:initial_sell_in) { -10 }

        it 'has 0 quality' do
          update_quality([item])
          expect(item.quality).to eq(0)
        end
      end
    end

    context "conjured item" do
      let(:name) { "Conjured Mana Cake" }

      it_behaves_like 'decrements sell_in', 1

      context "before the sell date" do
        let(:initial_sell_in) { 5 }

        it_behaves_like 'decrements quality', 2

        context "at zero quality" do
          let(:initial_quality) { 0 }

          it_behaves_like 'decrements quality', 0
        end
      end

      context "on sell date" do
        let(:initial_sell_in) { 0 }

        it_behaves_like 'decrements quality', 4

        context "at zero quality" do
          let(:initial_quality) { 0 }

          it_behaves_like 'decrements quality', 0
        end
      end

      context "after sell date" do
        let(:initial_sell_in) { -10 }

        it_behaves_like 'decrements quality', 4

        context "at zero quality" do
          let(:initial_quality) { 0 }
          it_behaves_like 'decrements quality', 0
        end
      end
    end
  end

  context "with several objects" do
    let(:items) {
      [
        Item.new("NORMAL ITEM", 5, 10),
        Item.new("Aged Brie", 3, 10),
      ]
    }

    before do
      update_quality(items)
    end

    it 'the first item is correctly updated' do
      expect(items[0].quality).to eq(9)
      expect(items[0].sell_in).to eq(4)
    end

    it 'the second item is correctly updated' do
      expect(items[1].quality).to eq(11)
      expect(items[1].sell_in).to eq(2)
    end
  end
end
